from evennia import default_cmds
from commands.dynamic_command_loader import setup_dynamic_commands


class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The `CharacterCmdSet` contains general in-game commands like `look`,
    `get`, etc., available on in-game Character objects.
    It is merged with the `AccountCmdSet` when an Account puppets a Character.
    """

    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the command set.
        """
        super().at_cmdset_creation()
        setup_dynamic_commands(self)  # Dynamically load commands from the dynamic folder


class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the command set available to the Account at all times.
    It is combined with the `CharacterCmdSet` when the Account puppets a Character.
    """

    key = "DefaultAccount"

    def at_cmdset_creation(self):
        """
        Populates the command set.
        """
        super().at_cmdset_creation()


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in.
    This holds commands like creating a new account, logging in, etc.
    """

    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the command set.
        """
        super().at_cmdset_creation()


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    Command set available at the Session level after logging in.
    It is empty by default.
    """

    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        Populates the command set.
        """
        super().at_cmdset_creation()
