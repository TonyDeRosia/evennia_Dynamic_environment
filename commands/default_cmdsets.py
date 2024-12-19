<<<<<<< HEAD
from evennia import default_cmds
from commands.dynamic_command_loader import setup_dynamic_commands

=======
"""
Command sets

All commands in the game must be grouped in a cmdset. A given command
can be part of any number of cmdsets and cmdsets can be added/removed
and merged onto entities at runtime.

To create new commands to populate the cmdset, see
`commands/command.py`.

This module wraps the default command sets of Evennia; overloads them
to add/remove commands from the default lineup. You can create your
own cmdsets by inheriting from them or directly from `evennia.CmdSet`.
"""

from evennia import default_cmds
from . import dynamic_loader
from evennia.utils.logger import log_info
>>>>>>> ba91aec (Backup of the project)

class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
<<<<<<< HEAD
    `get`, etc., available on in-game Character objects.
    It is merged with the `AccountCmdSet` when an Account puppets a Character.
    """

=======
    `get`, etc available on in-game Character objects. It is merged with
    the `AccountCmdSet` when an Account puppets a Character.
    """
>>>>>>> ba91aec (Backup of the project)
    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
<<<<<<< HEAD
        Populates the command set.
        """
        super().at_cmdset_creation()
        setup_dynamic_commands(self)  # Dynamically load commands from the dynamic folder


class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the command set available to the Account at all times.
    It is combined with the `CharacterCmdSet` when the Account puppets a Character.
    """

=======
        Populates the cmdset
        """
        super().at_cmdset_creation()
        # Load dynamic commands and add them to the CharacterCmdSet
        dynamic_cmdset = dynamic_loader.load_dynamic_commands()
        self.add(dynamic_cmdset)
        log_info(f"Dynamic commands successfully added to {self.key}")

class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the cmdset available to the Account at all times. It is
    combined with the `CharacterCmdSet` when the Account puppets a
    Character. It holds game-account-specific commands, channel
    commands, etc.
    """
>>>>>>> ba91aec (Backup of the project)
    key = "DefaultAccount"

    def at_cmdset_creation(self):
        """
<<<<<<< HEAD
        Populates the command set.
        """
        super().at_cmdset_creation()


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.
    This holds commands like creating a new account, logging in, etc.
    """

=======
        Populates the cmdset
        """
        super().at_cmdset_creation()

class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in. This
    holds commands like creating a new account, logging in, etc.
    """
>>>>>>> ba91aec (Backup of the project)
    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
<<<<<<< HEAD
        Populates the command set.
        """
        super().at_cmdset_creation()


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    Command set available at the Session level after logging in.
    It is empty by default.
    """

=======
        Populates the cmdset
        """
        super().at_cmdset_creation()

class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It
    is empty by default.
    """
>>>>>>> ba91aec (Backup of the project)
    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
<<<<<<< HEAD
        Populates the command set.
=======
        This is the only method defined in a cmdset, called during
        its creation. It should populate the set with command instances.
>>>>>>> ba91aec (Backup of the project)
        """
        super().at_cmdset_creation()
