from evennia import Command

from evennia.commands.cmdset import CmdSet



# Comprehensive Emotes Dictionary

EMOTES = {

    "wave": {

        "self": "You wave cheerfully.",

        "room": "{actor} waves cheerfully.",

        "target": "You wave at {target} enthusiastically.",

        "target_room": "{actor} waves at {target} enthusiastically.",

    },

    "hi": {

        "self": "You say hi enthusiastically.",

        "room": "{actor} says hi enthusiastically.",

        "target": "You say hi to {target}.",

        "target_room": "{actor} says hi to {target}.",

    },

    "hello": {

        "self": "You greet everyone with a cheerful hello.",

        "room": "{actor} greets everyone with a cheerful hello.",

        "target": "You greet {target} warmly.",

        "target_room": "{actor} greets {target} warmly.",

    },

    "greet": {

        "self": "You greet everyone around you.",

        "room": "{actor} greets everyone around them.",

        "target": "You greet {target} politely.",

        "target_room": "{actor} greets {target} politely.",

    },

    "greetings": {

        "self": "You offer a formal greeting.",

        "room": "{actor} offers a formal greeting.",

        "target": "You offer a formal greeting to {target}.",

        "target_room": "{actor} offers a formal greeting to {target}.",

    },

    "goodbye": {

        "self": "You wave goodbye.",

        "room": "{actor} waves goodbye.",

        "target": "You wave goodbye to {target}.",

        "target_room": "{actor} waves goodbye to {target}.",

    },

    "farewell": {

        "self": "You say farewell with a gentle nod.",

        "room": "{actor} says farewell with a gentle nod.",

        "target": "You bid {target} farewell.",

        "target_room": "{actor} bids {target} farewell.",

    },

    "apologize": {

        "self": "You apologize sincerely.",

        "room": "{actor} apologizes sincerely.",

        "target": "You apologize to {target}.",

        "target_room": "{actor} apologizes to {target}.",

    },

    "thank": {

        "self": "You thank everyone warmly.",

        "room": "{actor} thanks everyone warmly.",

        "target": "You thank {target} sincerely.",

        "target_room": "{actor} thanks {target} sincerely.",

    },

    "welcome": {

        "self": "You warmly welcome everyone.",

        "room": "{actor} warmly welcomes everyone.",

        "target": "You warmly welcome {target}.",

        "target_room": "{actor} warmly welcomes {target}.",

    },

    "salute": {

        "self": "You give a crisp salute.",

        "room": "{actor} gives a crisp salute.",

        "target": "You salute {target} smartly.",

        "target_room": "{actor} salutes {target} smartly.",

    },

    "smile": {

        "self": "You smile warmly.",

        "room": "{actor} smiles warmly.",

        "target": "You smile at {target}.",

        "target_room": "{actor} smiles at {target}.",

    },

    "laugh": {

        "self": "You laugh out loud.",

        "room": "{actor} laughs out loud.",

        "target": "You laugh with {target}.",

        "target_room": "{actor} laughs with {target}.",

    },

    "cry": {

        "self": "You cry softly.",

        "room": "{actor} cries softly.",

        "target": "You cry on {target}'s shoulder.",

        "target_room": "{actor} cries on {target}'s shoulder.",

    },

    "hug": {

        "self": "You hug yourself for comfort.",

        "room": "{actor} hugs themselves for comfort.",

        "target": "You hug {target} warmly.",

        "target_room": "{actor} hugs {target} warmly.",

    },

    "nod": {

        "self": "You nod approvingly.",

        "room": "{actor} nods approvingly.",

        "target": "You nod at {target} in agreement.",

        "target_room": "{actor} nods at {target} in agreement.",

    },

    "shrug": {

        "self": "You shrug helplessly.",

        "room": "{actor} shrugs helplessly.",

        "target": "You shrug at {target}.",

        "target_room": "{actor} shrugs at {target}.",

    },

    "clap": {

        "self": "You clap your hands.",

        "room": "{actor} claps their hands.",

        "target": "You clap for {target}.",

        "target_room": "{actor} claps for {target}.",

    },

    "cheer": {

        "self": "You cheer enthusiastically.",

        "room": "{actor} cheers enthusiastically.",

        "target": "You cheer for {target}.",

        "target_room": "{actor} cheers for {target}.",

    },

    "facepalm": {

        "self": "You facepalm.",

        "room": "{actor} facepalms.",

        "target": "You facepalm at {target}.",

        "target_room": "{actor} facepalms at {target}.",

    },

    "bow": {

        "self": "You bow deeply.",

        "room": "{actor} bows deeply.",

        "target": "You bow respectfully to {target}.",

        "target_room": "{actor} bows respectfully to {target}.",

    },

    "dance": {

        "self": "You dance around happily.",

        "room": "{actor} dances around happily.",

        "target": "You dance with {target}.",

        "target_room": "{actor} dances with {target}.",

    },

    "sigh": {

        "self": "You let out a deep sigh.",

        "room": "{actor} lets out a deep sigh.",

        "target": "You sigh at {target}.",

        "target_room": "{actor} sighs at {target}.",

    },

    "think": {

        "self": "You pause to think deeply.",

        "room": "{actor} pauses to think deeply.",

        "target": "You think about {target}.",

        "target_room": "{actor} thinks about {target}.",

    },

    "applaud": {

        "self": "You applaud enthusiastically.",

        "room": "{actor} applauds enthusiastically.",

        "target": "You applaud {target}.",

        "target_room": "{actor} applauds {target}.",

    },

    "yawn": {

        "self": "You yawn loudly.",

        "room": "{actor} yawns loudly.",

        "target": "You yawn at {target}.",

        "target_room": "{actor} yawns at {target}.",

    },

    "wink": {

        "self": "You wink mischievously.",

        "room": "{actor} winks mischievously.",

        "target": "You wink at {target}.",

        "target_room": "{actor} winks at {target}.",

    },

    "blush": {

        "self": "You blush deeply.",

        "room": "{actor} blushes deeply.",

        "target": "You blush at {target}.",

        "target_room": "{actor} blushes at {target}.",

    },

    "whistle": {

        "self": "You whistle a cheerful tune.",

        "room": "{actor} whistles a cheerful tune.",

        "target": "You whistle at {target} appreciatively.",

        "target_room": "{actor} whistles at {target} appreciatively.",

    },

    "nod": {

        "self": "You nod slightly.",

        "room": "{actor} nods slightly.",

        "target": "You nod at {target}.",

        "target_room": "{actor} nods at {target}.",

    },

    "giggle": {

        "self": "You giggle softly.",

        "room": "{actor} giggles softly.",

        "target": "You giggle at {target}.",

        "target_room": "{actor} giggles at {target}.",

    },

    "grin": {

        "self": "You grin widely.",

        "room": "{actor} grins widely.",

        "target": "You grin at {target}.",

        "target_room": "{actor} grins at {target}.",

    }

}



class CmdEmote(Command):

    """

    Base command for emotes.



    Usage:

        <emote>            - Perform an emote (e.g., wave)

        <emote> <target>   - Perform an emote targeting another player/object (e.g., wave Bob)

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



        if not target_name:

            # No target specified

            self.caller.msg(emote_data["self"])

            self.caller.location.msg_contents(

                emote_data.get("room", "").format(actor=self.caller),

                exclude=self.caller,

            )

            return



        target = self.caller.search(target_name)

        if not target:

            self.caller.msg(f"You don't see '{target_name}' here.")

            return



        # Target specified

        if "target" in emote_data:

            self.caller.msg(emote_data["target"].format(target=target))

        if "target_room" in emote_data:

            self.caller.location.msg_contents(

                emote_data["target_room"].format(actor=self.caller, target=target),

                exclude=[self.caller, target],

            )

        if target != self.caller:

            target.msg(emote_data["target_room"].format(actor=self.caller, target=target))



# Create individual command classes for each emote

emote_commands = []

for emote_name in EMOTES.keys():

    cmd_class = type(

        f"Cmd{emote_name.capitalize()}",

        (CmdEmote,),

        {"key": emote_name, "__doc__": f"Perform the {emote_name} emote."},

    )

    emote_commands.append(cmd_class)



# Make commands accessible at module level for the dynamic loader

for cmd in emote_commands:

    globals()[cmd.__name__] = cmd
