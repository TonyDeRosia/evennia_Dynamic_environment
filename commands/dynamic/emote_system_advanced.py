from evennia import Command
from evennia.commands.cmdset import CmdSet

    },
    "clap": {
        "self": "You clap your hands.",
        "room": "{actor} claps their hands.",
    },
    "applaud": {
        "self": "You applaud enthusiastically.",
        "room": "{actor} applauds enthusiastically.",
}

class CmdEmote(Command):
    """
    locks = "cmd:all()"

    def parse(self):
        """Parse the command arguments."""
        self.args = self.args.strip()

    def func(self):
        """Execute the emote logic."""
        emote = self.key.lower()
        target_name = self.args

        if emote not in EMOTES:
            self.caller.msg("That emote is not available.")
            return

        emote_data = EMOTES[emote]

        if not target:
            self.caller.msg(f"You don't see '{target_name}' here.")
            return

        if "target" in emote_data:
            self.caller.msg(emote_data["target"].format(target=target))
        if "target_room" in emote_data:
            self.caller.location.msg_contents(
                emote_data["target_room"].format(actor=self.caller, target=target),
                exclude=[self.caller, target],
            )
        if target != self.caller:
            target.msg(emote_data["target_room"].format(actor=self.caller, target=target))

