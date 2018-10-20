## Settings for game speed.
# The time in seconds between ticks.
game_speed = 0.1
# The time in seconds between the next automatic fight.
time_between_fights = 3
# Attempt to edit between fights or not:
pause_on_fight = False

## settings for xp gain, requirements and levelup.
# The number of free stat points a player earns on level up.
points_per_level = 3
# The XP granted by each mob.
mob_xp = 5
# The constant to scale XP requirements by as a function of level.
xp_scale = 2
# The exponent to scale XP requirements by as a function of level.
xp_exp = 2
# If xp_reset is True, then every level resets player XP to 0.
xp_reset = True

## Defaults for the starting Player.
default_name = "Pseu"
default_strength = 5
default_constitution = 5
default_free_points = 0
default_level = 1
default_xp = 0

## Defaults for mob spawning.
# The length of a mob name.
name_length = 4
# The variance in stats for new mobs being generated.
variance = (0.5, 1.5)

## Data regarding edit mode:
edit_prompt = "Provide a string to allocate points.\n"\
              "  Every 's' adds a point to strength,\n"\
              "  every 'c' adds a point to constitution.\n"\
              "  The character 'e' and the empty string exits.\n"\
              "  'z' changes zones.\n"\
              "  And 'q' quits the game.\n"
# The characters in the edit strings
# when a key needs to be generated on-the-fly 
# (e.g. for a zone list), this is where they're picked from.
key_order = list('asdfqwerzxcvgtbhyn')
# to allocate stat points or exit edit mode.
add_strength_chars = ['s', 'r']
add_constitution_chars = ['c', 'n']
exit_chars = ['e', 'x']
quit_chars = ['q']
zone_chars = ['z']
