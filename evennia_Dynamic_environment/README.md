# evennia_Dynamic_environment
This Evennia project uses a dynamic auto loader script so all you do is drop py files into the dynamic folder and they will work automatically.

    Dynamic Command Auto-Loader:
        Commands placed in the commands/dynamic folder are automatically discovered and loaded at runtime using the command_auto_loader.py.
        No manual edits to default_cmdsets.py or hardcoding of individual commands are needed—just drop your .py file into the dynamic folder, and the auto-loader takes care of the rest.

    Scripts Folder for Persistent Systems:
        The commands/scripts folder is reserved for implementing persistent game systems such as combat mechanics, buffs, and prompts.
        These scripts are modular and interact seamlessly with commands or game objects, ensuring maintainability and clarity.

    Clean Setup:
        Core Evennia files, like default_cmdsets.py and settings.py, remain unmodified.
        All customizations are isolated within the commands/dynamic and commands/scripts folders, adhering to Evennia's best practices for extensibility.

    Advanced Emote System:
        A robust emote system dynamically generates commands for predefined emotes like hello, wave, and spit.
        This allows for immersive and dynamic interactions without the overhead of manually defining each emote command.

How the Auto-Loader Works

The command_auto_loader.py:

    Dynamically scans the commands/dynamic folder for .py files.
    Automatically loads command classes (subclasses of Evennia’s Command) and adds them to the game's command set.
    This eliminates the need to register commands manually, making it quick and intuitive to add or update game features.

Example Workflow:

    Create a new Python file in commands/dynamic/.
    Define your command class (e.g., class CmdWave(Command)).
    Reload the server (evennia reload), and the command is ready to use in the game.

Scripts Folder Usage

The commands/scripts folder is dedicated to persistent and reusable systems that require continuous updates or interaction with game objects. Examples include:

    Player buff management.
    Real-time stat tracking.
    Combat or economic systems.

Scripts in this folder typically use Evennia's DefaultScript or interact with TICKER_HANDLER for periodic updates.

Modularity:

    All commands, scripts, and systems are standalone and self-contained.
    New features can be added without impacting existing functionality.

Dynamic Loading:

    The dynamic folder handles commands, while the scripts folder is reserved for systems.
    Developers can focus on implementing features instead of managing configuration files.

Seamless Integration:

    The auto-loader ensures commands are added automatically, while scripts are tied to objects or server events using Evennia's lifecycle hooks (at_server_start, at_script_creation, etc.).

Future-Proof Design:

    The setup avoids modifying Evennia defaults, making it easier to update Evennia versions or migrate features to other projects.

