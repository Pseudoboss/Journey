import time
import random

import config
import exceptions
import entity
import zones

def attack_round(attacker, target):
    """the attacker and target both attack, 
    the result is formatted and printed."""
    attacker_attack = attacker.attack(target)
    target_attack = target.attack(attacker)

    attacker_string = ("{0: >{3}}/{1: <{3}}>{2: <2}"
        .format( attacker.health
               , attacker.max_health
               , attacker_attack.damage
               , len(str(attacker.max_health))))

    target_string = ("{0: >2}<{1: >{3}}/{2:<{3}}"
        .format( target_attack.damage
               , target.health
               , target.max_health
               , len(str(target.max_health))))

    print("{} | {}".format( attacker_string
                          , target_string))

def fight(player, target, speed=config.game_speed):
    """Start one fight, 
    Will break out of loop when either the player or target dies, 
    or if a KeyboardInterrupt occurs."""
    try:
        while True:
            attack_round(player, target)
            time.sleep(speed)
    except exceptions.DeathException as exception:
        print(exception.msg_str)
        exception.attack.attacker.win_against(exception.caller)
        if config.pause_on_fight: 
            player.edit()
    except KeyboardInterrupt:
        print("paused by KeyboardInterrupt")
        player.edit()

    player.full_regen()
    target = player.zone.create_mob(player)
    print("next fight in")
    for x in range(config.time_between_fights, 0, -1):
        print("  {}".format(x))
        time.sleep(1)
    fight(player, target, speed)
