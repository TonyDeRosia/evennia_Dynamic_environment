import sys
import importlib.util
from pathlib import Path
from evennia import Command, CmdSet
from evennia.utils.logger import log_info, log_err

class DynamicCommandSet(CmdSet):
    """
    Cmdset for dynamically loaded commands.
    """
    key = "dynamic_commands"
    priority = 1

def load_dynamic_commands():
    """
    Dynamically load all commands from the dynamic directory.
    Returns a CmdSet containing all successfully loaded commands.
    """
    dynamic_cmdset = DynamicCommandSet()
    dynamic_dir = Path(__file__).parent / "dynamic"

    if not dynamic_dir.exists():
        log_err(f"Dynamic directory {dynamic_dir} does not exist.")
        return dynamic_cmdset

    if str(dynamic_dir) not in sys.path:
        sys.path.append(str(dynamic_dir))

    for filepath in dynamic_dir.glob("*.py"):
        if filepath.name == "__init__.py":
            continue
        try:
            module_name = f"commands.dynamic.{filepath.stem}"
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr, Command) and attr is not Command:
                    dynamic_cmdset.add(attr())
                    log_info(f"Loaded dynamic command: {attr.__name__} ({attr.key})")
        except Exception as e:
            log_err(f"Error loading {filepath.name}: {str(e)}")
    return dynamic_cmdset
