
import os
import importlib.util
from evennia.utils import logger
from evennia import Command

def setup_dynamic_commands(cmdset):
    """
    Automatically load commands from the dynamic folder.
    """
    dynamic_dir = os.path.join(os.path.dirname(__file__), "dynamic")
    if not os.path.exists(dynamic_dir):
        logger.log_err("[ERROR] Dynamic directory does not exist.")
        return

    for filename in os.listdir(dynamic_dir):
        if filename.endswith(".py") and not filename.startswith("__"):
            filepath = os.path.join(dynamic_dir, filename)
            module_name = f"commands.dynamic.{filename[:-3]}"

            try:
                spec = importlib.util.spec_from_file_location(module_name, filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    if isinstance(attr, type) and issubclass(attr, Command) and attr is not Command:
                        cmdset.add(attr())
                        logger.log_info(f"[INFO] Loaded command: {attr.key} from {filename}")
            except Exception as e:
                logger.log_err(f"[ERROR] Failed to load command from {filename}: {e}")
