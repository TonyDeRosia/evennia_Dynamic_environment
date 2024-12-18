from evennia import Command
from evennia.commands.cmdset import CmdSet

# Additional Emotes
MORE_EMOTES = {
    "shiver": {
        "self": "You shiver from the cold.",
        "room": "{actor} shivers from the cold.",
    },
    "snarl": {
        "self": "You snarl angrily.",
        "target": "You snarl angrily at {target}.",
        "target_room": "{actor} snarls angrily at {target}.",
        "room": "{actor} snarls angrily.",
    },
    "grimace": {
        "self": "You grimace in discomfort.",
        "room": "{actor} grimaces in discomfort.",
    },
    "pat": {
        "self": "You pat yourself reassuringly.",
        "target": "You pat {target} on the shoulder.",
        "target_room": "{actor} pats {target} on the shoulder.",
        "room": "{actor} pats themselves reassuringly.",
    },
    "chortle": {
        "self": "You chortle with glee.",
        "room": "{actor} chortles with glee.",
    },
    "greet": {
        "self": "You greet everyone warmly.",
        "target": "You greet {target} with a smile.",
        "target_room": "{actor} greets {target} with a smile.",
        "room": "{actor} greets everyone warmly.",
    },
    "mock": {
        "self": "You mock the situation with exaggerated gestures.",
        "target": "You mock {target} playfully.",
        "target_room": "{actor} mocks {target} playfully.",
        "room": "{actor} mocks the situation with exaggerated gestures.",
    },
    "tiphat": {
        "self": "You tip your hat courteously.",
        "target": "You tip your hat to {target}.",
        "target_room": "{actor} tips their hat to {target}.",
        "room": "{actor} tips their hat courteously.",
    },
    "sulk": {
        "self": "You sulk in the corner.",
        "room": "{actor} sulks in the corner.",
    },
    "gawk": {
        "self": "You gawk in amazement.",
        "room": "{actor} gawks in amazement.",
    },
    "wink": {
        "self": "You wink slyly.",
        "target": "You wink slyly at {target}.",
        "target_room": "{actor} winks slyly at {target}.",
        "room": "{actor} winks slyly.",
    },
    "nudge": {
        "self": "You nudge yourself knowingly.",
        "target": "You nudge {target} to get their attention.",
        "target_room": "{actor} nudges {target} to get their attention.",
        "room": "{actor} nudges themselves knowingly.",
    },
    "snap": {
        "self": "You snap your fingers rhythmically.",
        "room": "{actor} snaps their fingers rhythmically.",
    },
    "tap": {
        "self": "You tap your foot impatiently.",
        "room": "{actor} taps their foot impatiently.",
    },
    "sigh": {
        "self": "You sigh heavily.",
        "room": "{actor} sighs heavily.",
    },
    "snicker": {
        "self": "You snicker quietly to yourself.",
        "room": "{actor} snickers quietly.",
    },
    "huff": {
        "self": "You huff indignantly.",
        "room": "{actor} huffs indignantly.",
    },
    "bowdeep": {
        "self": "You bow deeply with great respect.",
        "target": "You bow deeply to {target} with great respect.",
        "target_room": "{actor} bows deeply to {target} with great respect.",
        "room": "{actor} bows deeply with great respect.",
    },
    "groan": {
        "self": "You groan loudly in frustration.",
        "room": "{actor} groans loudly in frustration.",
    },
    "stretch": {
        "self": "You stretch your arms wide.",
        "room": "{actor} stretches their arms wide.",
    },
    "peer": {
        "self": "You peer intently at nothing in particular.",
        "target": "You peer intently at {target}.",
        "target_room": "{actor} peers intently at {target}.",
        "room": "{actor} peers intently at nothing in particular.",
    },
    "cheer": {
        "self": "You cheer enthusiastically.",
        "room": "{actor} cheers enthusiastically.",
    },
    "fidget": {
        "self": "You fidget nervously.",
        "room": "{actor} fidgets nervously.",
    },
    "blink": {
        "self": "You blink in confusion.",
        "room": "{actor} blinks in confusion.",
    },
    "scowl": {
        "self": "You scowl angrily.",
        "target": "You scowl angrily at {target}.",
        "target_room": "{actor} scowls angrily at {target}.",
        "room": "{actor} scowls angrily.",
    },
    "howl": {
        "self": "You let out a mournful howl.",
        "room": "{actor} lets out a mournful howl.",
    },
    "giggle": {
        "self": "You giggle playfully.",
        "room": "{actor} giggles playfully.",
    },
    "smirk": {
        "self": "You smirk knowingly.",
        "room": "{actor} smirks knowingly.",
    },
    "hop": {
        "self": "You hop excitedly.",
        "room": "{actor} hops excitedly.",
    },
    "roll": {
        "self": "You roll your eyes dramatically.",
        "room": "{actor} rolls their eyes dramatically.",
    },
    "sniff": {
        "self": "You sniff the air curiously.",
        "room": "{actor} sniffs the air curiously.",
    },
    "chuckle": {
        "self": "You chuckle softly to yourself.",
        "room": "{actor} chuckles softly.",
    },
}

class CmdEmote2(Command):
    """
    Base command for additional emotes.

    Usage:
        <emote>            - Perform an emote (e.g., shiver).
        <emote> <target>   - Perform an emote targeting another player/object (e.g., snarl Bob).
    """
    key = "emote2"
    locks = "cmd:all()"

    def parse(self):
        """Parse the command arguments."""
        self.args = self.args.strip()

    def func(self):
        """Execute the emote logic."""
        emote = self.key.lower()
        target_name = self.args

        if emote not in MORE_EMOTES:
            self.caller.msg("That emote is not available.")
            return

        emote_data = MORE_EMOTES[emote]

        if not target_name:
            self.caller.msg(emote_data["self"])
            self.caller.location.msg_contents(
                emote_data.get("room", ""), exclude=self.caller, mapping={"actor": self.caller}
            )
            return

        target = self.caller.search(target_name, quiet=True)
        if not target:
            self.caller.msg(f"You don't see '{target_name}' here.")
            return

        target = target[0]
        if "target" in emote_data:
            self.caller.msg(emote_data["target"].format(target=target))
        if "target_room" in emote_data:
            self.caller.location.msg_contents(
                emote_data["target_room"].format(actor=self.caller, target=target),
                exclude=[self.caller, target],
            )
        if target != self.caller:
            target.msg(emote_data["target_room"].format(actor=self.caller, target=target))

class MoreEmoteCmdSet(CmdSet):
    """
    CmdSet to include all additional emotes.
    """
    def at_cmdset_creation(self):
        """Add more emotes dynamically from the MORE_EMOTES dictionary."""
        for emote in MORE_EMOTES.keys():
            cmd = type(f"Cmd{emote.capitalize()}2", (CmdEmote2,), {"key": emote})
            self.add(cmd())
