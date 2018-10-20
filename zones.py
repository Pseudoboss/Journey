import random

import string
import config
import entity

def create_name(name_length = config.name_length):
    """Create a new random mob name.

    Parameters
    ----------
    name_length : int
        The length of the randomly-generated name

    Returns
    -------
    string
        The generated mob name.

    """
    name = [random.choice(string.ascii_lowercase) 
            for _ in range(name_length)]
    name = "".join(name)
    name = name.capitalize()
    return name

class Zone:
    """The generic Zone class which all zones inherit from.

    Attributes
    ----------
    name : str
        the name of the Zone.

    level : str
        the average level of mobs spawned by the Zone.
        Will be 's' if the zone scales with player level.

    """

    name = ''
    level = ''

    def __init__(self):
        pass

    def create_mob(self, player):
        """Spawn a new mob, randomly generating any required fields.

        Parameters
        ----------
        player : Player
            the Player entity to generate a fair mob based on.

        """
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
    """Manages and provides access tools for all implemented zones.

    AllZones is able to detect the available zones via Zone.__subclasses__().

    """

    def __init__(self):
        """initalize the AllZones class.

        """
        self.all_zones = []
        for zone in Zone.__subclasses__():
            self.all_zones.append(zone())
        self.all_zones.sort(key=lambda z: z.name)

    def dict(self, key_order = config.key_order):
        """Return a dictionary that maps keys to zones.

        Parameters
        ----------
        key_order : iterable of str
            The keys that will be assigned to zones.

        Returns
        -------
        dict
            The dictionary of keys mapped to all available zones.

        """
        return {key:zone for key, zone in zip(config.key_order, self.all_zones)}

    def table(self, cols = ["key", "name"], sep=" ", end="\n"):
        """Return a textual table of all zones.

        Parameters
        ----------
        cols : list of str
            The list of the columns to display.
            Possible values are "key" and "name".
        sep : str
            The string inserted between columns.
        end : str
            The string used to terminate a line.

        Returns
        -------
        str
            The formatted table requested.

        """
        print_key = "key" in cols
        print_name = "name" in cols
        o = ""
        for key, zone in zip(config.key_order, self.all_zones):
            o += key+sep+zone.name+end
        return o

all_zones = AllZones()
