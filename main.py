import player
import gameMaster
import config
import zones

if __name__ == "__main__":
    print()
    player = player.Player(config.default_name)
    enemy = player.zone.create_mob(player)
    gameMaster.fight(player, enemy)
