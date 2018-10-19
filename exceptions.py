########################################################################

class PauseException(Exception):
    """A PauseException is raised on any pause event."""
    pass

class DeathException(PauseException):
    """A DeathException is raised when an Entity dies."""
    def __init__(self, caller, attack, msg_str = None):
        self.caller = caller
        self.attack = attack

        if not msg_str:
            msg_str = f"{self.caller.name} dies to "\
                      f"{self.attack.attacker.name}!"
        self.msg_str = msg_str

        super().__init__(self.msg_str)