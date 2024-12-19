<<<<<<< HEAD
# Welcome to Evennia Dynamic Environment!

This project is designed as a base for creating MUDs (Multi-User Dungeons) or other text-based multiplayer games using Evennia. It includes a clean, ready-to-use setup with dynamic auto-loading capabilities to streamline game development.

Features
Dynamic Command and Script Loader:

Automatically detects and loads custom commands and scripts placed in the dynamic/ folder.
Simplifies adding new features without modifying core Evennia files.
Promotes modular and extensible development practices.
Organized Game Structure:

Pre-configured folders for commands, scripts, typeclasses, and world data.
Includes README.md files in each folder to guide customization.
Easy Integration:

Designed to work out of the box with Evennia's default setup.
Ideal for creating new projects or enhancing existing ones.
Folder Structure
commands/: Contains core command-related files.

dynamic/: Drop custom commands here to be automatically loaded by the dynamic auto-loader.
scripts/: For managing reusable scripts.
server/: Contains server configuration and runtime files.

typeclasses/: Define custom game objects like characters, rooms, and items.

world/: Store world-building resources such as prototypes and batch command files.

Dynamic Auto-Loader
The dynamic auto-loader simplifies the process of adding new commands and scripts by automatically detecting .py files in the dynamic/ folder. Here's how it works:

Place your .py file (e.g., mycommand.py) in the commands/dynamic/ folder.
The auto-loader scans this folder at runtime, identifies valid commands or scripts, and registers them with the game.
No manual registration or core file modification is required.
Usage Example
To create a custom command:

Write a Python file (mycommand.py) and place it in commands/dynamic/.
Define your command using Evennia's command structure:
python
Copy code
from evennia import Command

class CmdMyCommand(Command):
    key = "mycommand"
    help_category = "General"

    def func(self):
        self.caller.msg("This is my custom command!")
Save the file, and the dynamic auto-loader will handle the rest. Your new command will be available in-game immediately after a server restart.
Getting Started
Requirements
Python 3.8+
Evennia (latest stable version)
Setup Instructions
Clone this repository:

bash
Copy code
git clone https://github.com/<your-repository-url>.git
cd <project-folder>
Install dependencies and initialize Evennia:

bash
Copy code
pip install evennia
evennia migrate
Start the server:

bash
Copy code
evennia start
Begin customizing your game by adding commands, scripts, and typeclasses.
=======
# Welcome to Evennia!

This is your game directory, set up to let you start with
your new game right away. An overview of this directory is found here:
https://github.com/evennia/evennia/wiki/Directory-Overview#the-game-directory

You can delete this readme file when you've read it and you can
re-arrange things in this game-directory to suit your own sense of
organisation (the only exception is the directory structure of the
`server/` directory, which Evennia expects). If you change the structure
you must however also edit/add to your settings file to tell Evennia
where to look for things.

Your game's main configuration file is found in
`server/conf/settings.py` (but you don't need to change it to get
started). If you just created this directory (which means you'll already
have a `virtualenv` running if you followed the default instructions),
`cd` to this directory then initialize a new database using

    evennia migrate

To start the server, stand in this directory and run

    evennia start

This will start the server, logging output to the console. Make
sure to create a superuser when asked. By default you can now connect
to your new game using a MUD client on `localhost`, port `4000`.  You can
also log into the web client by pointing a browser to
`http://localhost:4001`.

# Getting started

From here on you might want to look at one of the beginner tutorials:
http://github.com/evennia/evennia/wiki/Tutorials.

Evennia's documentation is here:
https://github.com/evennia/evennia/wiki.

Enjoy!
>>>>>>> ba91aec (Backup of the project)
