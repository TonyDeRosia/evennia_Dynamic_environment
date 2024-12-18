
from evennia import Command

class CmdHello(Command):
    key = "hello"
    help_category = "General"

    def func(self):
        self.caller.msg("Hello, world!")
