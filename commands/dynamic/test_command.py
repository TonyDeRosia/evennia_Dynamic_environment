from evennia import Command

class CmdTest(Command):
    """
    A test command
    
    Usage:
        test
    """
    key = "test"
    locks = "cmd:all()"
    
    def func(self):
        self.caller.msg("Dynamic command system is working!")
