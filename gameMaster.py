import time
import random

import config
import exceptions
import entity
import zones

def attack_round(attacker, target):
    """Format and print both the attacker and target attacking.

    Parameters
    ----------
    attacker : Entity or subclass of Entity
        The Entity that goes first in the round.
        Is attacked by the target
    target : Entity or subclass of Entity
        The Entity being attacked by the target

    """
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

def on_KeyboardInterrupt(player):
    """Called whenever the a KeyboardInterrupt occurs."""
    print("paused by KeyboardInterrupt")
    player.edit()

def fight(player, target, speed=config.game_speed):
    """Loop attack_rounds until there is a victor, handle interrupts as they occur.

    TODO
    ----
    Separate this function between the fight loop and interrupt handling.

    Parameters
    ----------
    player : Player
        The player that is currently fighting.
        Will be attacked by target.
    target : Entity
        The target that player is attacking.
        Will be attacked by player.
    speed : float
        delay between iterations in seconds.

    """
    try:
        try:
            while True:
                attack_round(player, target)
                time.sleep(speed)

        except exceptions.DeathException as exception:
            print(exception.msg_str)
            exception.attack.attacker.on_win(exception.caller)
            if config.pause_on_fight: 
                player.edit()
            print("next fight in")
            for x in range(config.time_between_fights, 0, -1):
                print("  {}".format(x))
                time.sleep(1)
    except KeyboardInterrupt:
        on_KeyboardInterrupt(player)

    player.full_regen()
    target = player.zone.create_mob(player)
    fight(player, target, speed)
