import entity
import config

class Player(entity.Entity):
    """The Player class."""
    def __init__( self
                , name
                , level=config.default_level
                , xp=config.default_xp
                , free_points=config.default_free_points
                , strength=config.default_strength
                , constitution=config.default_constitution):
        """instantiate a new Player instance."""
        self.free_points = free_points
        self.strength = strength
        self.constitution = constitution
        self.determine_stats()
        super().__init__( name, level, xp
                        , self.max_health
                        , self.damage_range)

    def determine_stats(self):
        """determine the secondary stats from primary stats"""
        self.max_health = 10*self.constitution
        damage_min = self.strength-5
        damage_max = self.strength+5
        self.damage_range = range(damage_min, damage_max+1)
        self.stats = { "strength": self.strength
                     , "constitution": self.constitution}

    def on_win(self, target):
        """Called when the Entity kills a target."""
        self.xp += target.xp
        self.check_for_level_up()

    def check_for_level_up(self):
        """Check if the player has the XP to gain a Level.
        Gain a level, if so."""
        if self.xp >= self.xp_required:
            self.level_up()

    def level_up(self):
        """Level up the Player."""
        self.level += 1
        self.free_points += config.points_per_level
        if config.xp_reset:
            self.xp = 0
        print(f"{self.name} is now level {self.level}.")
        self.check_for_level_up()

    @property
    def xp_required(self):
        """the amount of XP required to gain a level."""
        return config.xp_scale*self.level**config.xp_exp

    def edit(self):
        """Enter player managment mode."""
        if self.free_points <= 0:
            edit = False
        else:
            edit = True
            print(f"now editing {self.name}")

        while edit:
            print(self.charsheet)

            instr = input(config.edit_prompt)
            edit = self.process_stat_string(instr)

            self.determine_stats()

    def process_stat_string(self, string):
        """Process a given stat string, char-by-char.
        Returns whether edit mode should be exited."""
        edit = True
        strength_added = 0
        constitution_added = 0
        for char in string:
            if char in config.add_strength_chars:
                self.strength += 1
                self.free_points -= 1
                strength_added += 1

            elif char in config.add_constitution_chars:
                self.constitution += 1
                self.free_points -= 1
                constitution_added += 1

            elif char in config.exit_chars:
                edit = False
                break

            elif char in config.quit_chars:
                quit()

            if self.free_points <= 0:
                edit = False
                break

        if strength_added == 0 and constitution_added == 0:
            print("exiting")
            edit = False
        else:
            print("added {} point{} to strength "\
                  "and {} point{} to constitution.".format
                  ( strength_added, 's'*(strength_added!=1)
                  , constitution_added, 's'*(constitution_added!=1)))

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
