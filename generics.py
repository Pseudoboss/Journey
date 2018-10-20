class Attack():
    """Contains information about the recent attack. 

    Information includes damage and a reference to the attacker.

    """
    def __init__(self, attacker, damage):
        """Initalize a new Attack.

        Parameters
        ----------
        attacker : Entity or subclass of Entity
            The attacker that is making the attack.
        damage : int
            The damage rolled by the attacker. 

        """
        self.attacker = attacker
        self.damage = damage
