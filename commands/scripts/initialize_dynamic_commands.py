from pathlib import Path
from evennia.utils.logger import log_info

def at_server_start():
    """
    Ensure the dynamic directory exists on server startup.
    """
    dynamic_dir = Path(__file__).parent.parent / "dynamic"
    if not dynamic_dir.exists():
        dynamic_dir.mkdir(parents=True, exist_ok=True)
        (dynamic_dir / "__init__.py").write_text("# Dynamic commands package\n")
        log_info(f"Created dynamic directory at {dynamic_dir}")
