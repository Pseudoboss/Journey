########################################################################

import random

import generics
import exceptions


class Entity:
    """The Entity class"""

    def __init__( self
                , name
                , level=1
                , xp=5
                , max_health=100
                , damage_range=range(1, 11)):
        """Instantiate a new Entity"""
        self.name = name
        self.level = level
        self.xp = 5
        self.max_health = max_health
        self.health = max_health
        self.damage_range = damage_range

    @property
    def xp(self):
        return self._xp

    @xp.setter
    def xp(self, value):
        self._xp = value

    @property
    def max_health(self):
        return self._max_health

    @max_health.setter
    def max_health(self, value):
        if value <= 0:
            raise ValueError("max_health cannot be 0 or less.")
        self._max_health = value

    @property
    def damage_range(self):
        return self._damage_range

    @damage_range.setter
    def damage_range(self, value):
        if list(value) == []:
            raise ValueError("damage_range cannot be empty.")
        self._damage_range = value

    def attack(self, target):
        """Attack the provided target, passing an Attack to it."""
        damage = random.choice(self.damage_range)
        attack = generics.Attack(self, damage)
        try:
            target.take_attack(attack)
        except exceptions.DeathException as death:
            self.on_win(target)
            raise death
        return attack

    def take_attack(self, attack):
        """Take the provided amount of damage."""
        self.health -= attack.damage
        if self.health <= 0:
            self.die(attack)
        return self.health

    def die(self, attack):
        """Die, raise DeathException to be handled elsewhere."""
        raise exceptions.DeathException(self, attack)

    def on_win(self, target):
        """Called when the Entity kills a target."""
        pass

    def full_regen(self):
        """Regenerate all health."""
        self.health = self.max_health
