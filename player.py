import entity
import config
import zones

class Player(entity.Entity):
    """Represents a player.

    Attributes
    ----------
    health : int
        The Player's current health.
        When it reaches 0 or below, the player dies.
    zone : Zone
        Zone that the player is in.

    """
    def __init__( self
                , name
                , level=config.default_level
                , xp=config.default_xp
                , free_points=config.default_free_points
                , strength=config.default_strength
                , constitution=config.default_constitution
                , zone=zones.all_zones.all_zones[0]):
        """instantiate a new Player instance.

        Parameters
        ----------
        name : str
            Name of the new Player
        level : int
            Level of the new Player.
            Should be directly proportional to power.
        xp : int
            Starting xp provided to the new player.
        free_points : int
            Starting free points for allocation by the player.
        strength : int
            Starting strength of the player.
            Determines the damage range.
        constitution : int
            Starting constitution of the player.
            Determines their max health.

        """
        self.free_points = free_points
        self.strength = strength
        self.constitution = constitution
        self._determins_stats()
        self.zone = zone
        super().__init__( name, level, xp
                        , self.max_health
                        , self.damage_range)

    def _determins_stats(self):
        """determine the secondary stats from primary stats.

        This method should not need to be used outside of this class.

        """
        self.max_health = 10*self.constitution
        damage_min = self.strength-5
        damage_max = self.strength+5
        self.damage_range = range(damage_min, damage_max+1)
        self.stats = { "strength": self.strength
                     , "constitution": self.constitution}

    def on_win(self, target):
        """Called when the Entity kills a target.

        Parameters
        ----------
        target : Entity or subclass of Entity
            The target the player has recently slain.

        """
        self.xp += target.xp
        self._check_for_level_up()

    def _check_for_level_up(self):
        """Check if the player has the XP to gain a Level. If so, gain a level.

        This method should not need to be used outside of this class.

        """
        if self.xp >= self.xp_required:
            self._level_up()

    def _level_up(self):
        """Level up the Player.

        This method should not need to be used outside of this class.
        If you want to provide a free level to the player, provide it by
        setting xp.

        """
        self.level += 1
        self.free_points += config.points_per_level
        if config.xp_reset:
            self.xp = 0
        print(f"{self.name} is now level {self.level}.")
        self._check_for_level_up()

    @property
    def xp_required(self):
        """the amount of XP required to reach the next level."""
        return config.xp_scale*self.level**config.xp_exp

    def edit(self):
        """Enter player managment mode.

        In player management mode, you can allocate free skill points, change
        zones, and exit the game.

        """
        edit = True
        print(f"now editing {self.name}")

        while edit:
            print(self.charsheet)

            instr = input(config.edit_prompt)
            edit = self.process_edit_string(instr)

            self._determins_stats()

    def process_edit_string(self, string):
        """Process a given edit string, char-by-char.

        Paramaters
        ----------
        string : str
            The edit string to process.

        Returns
        -------
        bool
            Whether edit mode should be exited.

        """
        edit = True
        strength_added = 0
        constitution_added = 0
        for char in string:
            if self.free_points > 0:
                if char in config.add_strength_chars:
                    self.strength += 1
                    self.free_points -= 1
                    strength_added += 1

                elif char in config.add_constitution_chars:
                    self.constitution += 1
                    self.free_points -= 1
                    constitution_added += 1

            if char in config.exit_chars:
                edit = False
                break

            elif char in config.zone_chars:
                self.edit_zone()

            elif char in config.quit_chars:
                quit()

        if strength_added == 0 and constitution_added == 0:
            print("No stat change.")

        else:
            print("added {} point{} to strength "\
                  "and {} point{} to constitution.".format
                  ( strength_added, 's'*(strength_added!=1)
                  , constitution_added, 's'*(constitution_added!=1)))

        return edit

    def edit_zone(self):
        """Edit the zone that the player is in.

        Returns
        -------
        bool
            Whether edit mode should be exited.

        """
        edit = True
        zone_options = zones.all_zones.dict()
        print(zones.all_zones.table())
        key = input("Enter a key: ")
        self.zone = zone_options[key]
        print(f"traveling to {self.zone.name}")
        return edit

    @property
    def charsheet(self):
        """a string containing important character information."""
        o =  f"name: {self.name}\n"
        o += f"free points: {self.free_points}\n"
        o += f"level: {self.level}\n"
        o += f"strength: {self.strength}\n"
        o += f"constitution: {self.constitution}\n"

        return o
