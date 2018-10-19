import random

import string
import config
import entity

def create_name(name_length = config.name_length):
    """Create a new random mob name."""
    name = [random.choice(string.ascii_lowercase) 
            for _ in range(name_length)]
    name = "".join(name)
    name = name.capitalize()
    return name

class Zone:
    """The generic Zone class which all zones inherit from."""
    def __init__(self):
        pass

    def create_mob(self, player):
        """Spawn a new mob, randomly generating any required fields."""
        name = create_name()
        health_min = int(player.health * min(config.variance))
        health_max = int(player.health * max(config.variance))
        health = random.randint(health_min, health_max)

        damage_limits = []
        damage_min = [int(min(player.damage_range)*x)
                      for x in config.variance]
        damage_limits.append(random.randint( min(damage_min)
                                           , max(damage_min)))

        damage_max = [int(max(player.damage_range)*x)
                      for x in config.variance]
        damage_limits.append(random.randint( min(damage_max)
                                           , max(damage_max)))

        if min(damage_limits) == max(damage_limits):
            damage_limits = [min(damage_limits), min(damage_limits)+1]

        damage_range = range(min(damage_limits), max(damage_limits))

        return entity.Entity( name
                            , max_health=health
                            , damage_range=damage_range)

class genericland(Zone):
    name = "Genericland"

class Spookwood(Zone):
    name = "Spookwood"

class Lavafield(Zone):
    name = "Lava Field"

class AllZones():
    def __init__(self):
        self.all_zones = []
        for zone in Zone.__subclasses__():
            self.all_zones.append(zone())
        self.all_zones.sort(key=lambda z: z.name)

    @property
    def table(self):
        o = ""
        for zone in self.all_zones:
            o += zone.name+"\n"
        return o

    def select(self, player):
        player.zone = self.all_zones[0]

all_zones = AllZones()

if __name__ == "__main__":
    print(all_zones.table)
