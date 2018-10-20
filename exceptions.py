class PauseException(Exception):
    """A PauseException is raised on any pause event."""
    pass

class DeathException(PauseException):
    """A DeathException is raised when an Entity dies."""

    def __init__(self, caller, attack, msg_str = None):
        """Instantiate a new DeathException to be raised.

        Paramaters
        ----------
        caller : Entity or subclass of Entity
            The Entity that recently died and is raising the DeathException.
        attack : Attack
            The Attack that struck down the caller.
        msg_str : str
            a human-readable string describing the exception.

        """
        self.caller = caller
        self.attack = attack

        if not msg_str:
            msg_str = f"{self.caller.name} dies to "\
                      f"{self.attack.attacker.name}!"
        self.msg_str = msg_str

        super().__init__(self.msg_str)
