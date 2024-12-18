#!/usr/bin/env python3

import os
import importlib.util
import traceback

# Constants
DYNAMIC_DIR = "dynamic"

# Simple logging function
def log(message, level="INFO"):
    """
    Logs messages to the console for debugging purposes.
    """
    levels = {"INFO": "[INFO]", "ERROR": "[ERROR]", "DEBUG": "[DEBUG]"}
    print(f"{levels.get(level, '[INFO]')} {message}")

def setup_dynamic_directory():
    """
    Ensure the dynamic directory and __init__.py file exist.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dynamic_dir_path = os.path.join(base_dir, DYNAMIC_DIR)

    # Create the dynamic directory if it doesn't exist
    if not os.path.exists(dynamic_dir_path):
        os.makedirs(dynamic_dir_path)
        log(f"Created dynamic directory at {dynamic_dir_path}", "INFO")

    # Ensure __init__.py exists
    init_file = os.path.join(dynamic_dir_path, "__init__.py")
    if not os.path.exists(init_file):
        with open(init_file, "w") as f:
            f.write("# This file makes the dynamic directory a Python package.\n")
        log(f"Created __init__.py in {dynamic_dir_path}", "INFO")

    return dynamic_dir_path

def scan_dynamic_commands():
    """
    Scan the dynamic directory for Python files containing Command subclasses.
    Returns a list of detected Command classes.
    """
    dynamic_dir_path = setup_dynamic_directory()
    commands = []

    for filename in os.listdir(dynamic_dir_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            filepath = os.path.join(dynamic_dir_path, filename)
            module_name = f"{DYNAMIC_DIR}.{filename[:-3]}"

            try:
                # Dynamically load the module
                spec = importlib.util.spec_from_file_location(module_name, filepath)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                for attr_name in dir(module):
                    attr = getattr(module, attr_name)
                    # Detect Command-like classes based on their structure
                    if isinstance(attr, type) and hasattr(attr, "key"):
                        commands.append(attr)
                        log(f"Detected command: {attr.key} in {filename}", "DEBUG")

            except Exception as e:
                if "Requested setting" in str(e):
                    log(f"Skipped {filename} due to Django dependency.", "WARNING")
                else:
                    log(f"Failed to load {filename}: {e}", "ERROR")
                    log(traceback.format_exc(), "DEBUG")

    return commands

def setup_dynamic_commands(cmdset):
    """
    Automatically load all commands from the dynamic directory into the given CmdSet.

    Args:
        cmdset (CmdSet): The command set to which dynamic commands will be added.
    """
    commands = scan_dynamic_commands()
    for command in commands:
        cmdset.add(command())
        log(f"Added command: {command.key} to CmdSet", "INFO")

def main():
    """
    Main function to orchestrate the dynamic command loader setup.
    """
    log("Starting dynamic command loader setup...", "INFO")

    # Scan for dynamic commands
    commands = scan_dynamic_commands()
    if not commands:
        log("No dynamic commands found or all skipped due to dependencies.", "WARNING")
    else:
        log(f"Found {len(commands)} dynamic commands.", "INFO")

    log("Dynamic command loader setup completed.", "INFO")

if __name__ == "__main__":
    main()
