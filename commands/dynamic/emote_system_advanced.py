from evennia import Command
from evennia.commands.cmdset import CmdSet

# Expanded Emote dictionary
EMOTES = {
    "spit": {
        "self": "You spit on the ground.",
        "room": "{actor} spits on the ground.",
    },
    "wave": {
        "self": "You wave your hand in the air.",
        "target": "You wave at {target}.",
        "target_room": "{actor} waves at {target}.",
        "room": "{actor} waves their hand in the air.",
    },
    "nod": {
        "self": "You nod to yourself.",
        "target": "You nod to {target}.",
        "target_room": "{actor} nods to {target}.",
        "room": "{actor} nods thoughtfully.",
    },
    "smile": {
        "self": "You smile warmly.",
        "target": "You smile warmly at {target}.",
        "target_room": "{actor} smiles warmly at {target}.",
        "room": "{actor} smiles warmly.",
    },
    "shrug": {
        "self": "You shrug nonchalantly.",
        "room": "{actor} shrugs nonchalantly.",
    },
    "laugh": {
        "self": "You laugh heartily.",
        "target": "You laugh at {target}'s antics.",
        "target_room": "{actor} laughs at {target}'s antics.",
        "room": "{actor} laughs heartily.",
    },
    "clap": {
        "self": "You clap your hands.",
        "room": "{actor} claps their hands.",
    },
    "blush": {
        "self": "You blush deeply.",
        "room": "{actor} blushes deeply.",
    },
    "cheer": {
        "self": "You cheer excitedly.",
        "room": "{actor} cheers excitedly.",
    },
    "wave": {
        "self": "You wave your hand in greeting.",
        "target": "You wave at {target} in greeting.",
        "target_room": "{actor} waves at {target} in greeting.",
        "room": "{actor} waves their hand in greeting.",
    },
    "dance": {
        "self": "You begin to dance gracefully.",
        "room": "{actor} begins to dance gracefully.",
    },
    "bow": {
        "self": "You bow deeply.",
        "target": "You bow respectfully to {target}.",
        "target_room": "{actor} bows respectfully to {target}.",
        "room": "{actor} bows deeply.",
    },
    "cry": {
        "self": "Tears roll down your cheeks.",
        "room": "Tears roll down {actor}'s cheeks.",
    },
    "cough": {
        "self": "You cough quietly.",
        "room": "{actor} coughs quietly.",
    },
    "whistle": {
        "self": "You whistle a merry tune.",
        "room": "{actor} whistles a merry tune.",
    },
    "stare": {
        "self": "You stare blankly ahead.",
        "target": "You stare at {target} intently.",
        "target_room": "{actor} stares at {target} intently.",
        "room": "{actor} stares blankly ahead.",
    },
    "yawn": {
        "self": "You yawn widely.",
        "room": "{actor} yawns widely.",
    },
    "grin": {
        "self": "You grin mischievously.",
        "target": "You grin mischievously at {target}.",
        "target_room": "{actor} grins mischievously at {target}.",
        "room": "{actor} grins mischievously.",
    },
    "applaud": {
        "self": "You applaud enthusiastically.",
        "room": "{actor} applauds enthusiastically.",
    },
    "frown": {
        "self": "You frown in disappointment.",
        "room": "{actor} frowns in disappointment.",
    },
    "gasp": {
        "self": "You gasp in surprise.",
        "room": "{actor} gasps in surprise.",
    },
    "chuckle": {
        "self": "You chuckle softly.",
        "room": "{actor} chuckles softly.",
    },
    "sneeze": {
        "self": "You sneeze loudly.",
        "room": "{actor} sneezes loudly.",
    },
    "facepalm": {
        "self": "You facepalm in disbelief.",
        "room": "{actor} facepalms in disbelief.",
    },
    "salute": {
        "self": "You salute smartly.",
        "target": "You salute {target} smartly.",
        "target_room": "{actor} salutes {target} smartly.",
        "room": "{actor} salutes smartly.",
    },
    "ponder": {
        "self": "You ponder the situation.",
        "room": "{actor} seems to ponder the situation.",
    },
    "wink": {
        "self": "You wink playfully.",
        "target": "You wink playfully at {target}.",
        "target_room": "{actor} winks playfully at {target}.",
        "room": "{actor} winks playfully.",
    },
    "hi": {
        "self": "You greet everyone with a cheerful 'Hi!'",
        "target": "You greet {target} with a cheerful 'Hi!'",
        "target_room": "{actor} greets {target} with a cheerful 'Hi!'",
        "room": "{actor} greets everyone with a cheerful 'Hi!'",
    },
    "hug": {
        "self": "You hug yourself.",
        "target": "You give {target} a warm hug.",
        "target_room": "{actor} gives {target} a warm hug.",
        "room": "{actor} hugs themselves.",
    },
}

class CmdEmote(Command):
    """
    Base command for all emotes.

    Usage:
        <emote>            - Perform an emote (e.g., wave).
        <emote> <target>   - Perform an emote targeting another player/object (e.g., wave Bob).
    """
    key = "emote"
    locks = "cmd:all()"

    def parse(self):
        """Parse the command arguments."""
        self.args = self.args.strip()

    def func(self):
        """Execute the emote logic."""
        # Determine emote and arguments
        emote = self.key.lower()
        target_name = self.args

        if emote not in EMOTES:
            self.caller.msg("That emote is not available.")
            return

        emote_data = EMOTES[emote]

        # Handle no target
        if not target_name:
            self.caller.msg(emote_data["self"])
            self.caller.location.msg_contents(
                emote_data.get("room", ""), exclude=self.caller, mapping={"actor": self.caller}
            )
            return

        # Handle targeted emotes
        target = self.caller.search(target_name, quiet=True)
        if not target:
            self.caller.msg(f"You don't see '{target_name}' here.")
            return

        target = target[0]  # Assume the first result if multiple are found
        if "target" in emote_data:
            self.caller.msg(emote_data["target"].format(target=target))
        if "target_room" in emote_data:
            self.caller.location.msg_contents(
                emote_data["target_room"].format(actor=self.caller, target=target),
                exclude=[self.caller, target],
            )
        if target != self.caller:
            target.msg(emote_data["target_room"].format(actor=self.caller, target=target))

class EmoteCmdSet(CmdSet):
    """
    CmdSet to include all emotes.
    """
    def at_cmdset_creation(self):
        """Add emotes dynamically from the EMOTES dictionary."""
        for emote in EMOTES.keys():
            cmd = type(f"Cmd{emote.capitalize()}", (CmdEmote,), {"key": emote})
            self.add(cmd())

