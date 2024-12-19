from evennia import default_cmds
from . import dynamic_loader
from evennia.utils.logger import log_info


class CharacterCmdSet(default_cmds.CharacterCmdSet):
    """
    The CharacterCmdSet contains general in-game commands like look, get, etc., 
    available on in-game Character objects. It is merged with the AccountCmdSet 
    when an Account puppets a Character.
    """

    key = "DefaultCharacter"

    def at_cmdset_creation(self):
        """
        Populates the cmdset.
        """
        super().at_cmdset_creation()
        dynamic_cmdset = dynamic_loader.load_dynamic_commands()
        self.add(dynamic_cmdset)
        log_info(f"Dynamic commands successfully added to {self.key}")


class AccountCmdSet(default_cmds.AccountCmdSet):
    """
    This is the cmdset available to the Account at all times. It is combined 
    with the CharacterCmdSet when the Account puppets a Character. It holds 
    game-account-specific commands, channel commands, etc.
    """

    key = "DefaultAccount"

    def at_cmdset_creation(self):
        """
        Populates the cmdset.
        """
        super().at_cmdset_creation()


class UnloggedinCmdSet(default_cmds.UnloggedinCmdSet):
    """
    Command set available to the Session before being logged in. This holds 
    commands like creating a new account, logging in, etc.
    """

    key = "DefaultUnloggedin"

    def at_cmdset_creation(self):
        """
        Populates the cmdset.
        """
        super().at_cmdset_creation()


class SessionCmdSet(default_cmds.SessionCmdSet):
    """
    This cmdset is made available on Session level once logged in. It is empty 
    by default.
    """

    key = "DefaultSession"

    def at_cmdset_creation(self):
        """
        Populates the cmdset.
        """
        super().at_cmdset_creation()
