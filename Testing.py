from Characters_info import Character
from Characters_info import gamestart
from Characters_info import store
from Characters_info import Battle
from Characters_info import FancyCloack
from Characters_info import SuperTonic
from Characters_info import Armor
from Characters_info import Tonic
from Characters_info import Sword
from Characters_info import Lottery
import random
import time


squire = Squire()
enemies = [Goblin(), Wizard(), Bandit(), Bandit(), Goblin(), Bandit(), Goblin(), Giant()]
battle_engine = Battle()
shopping_engine = Store()

gamestart()
for enemy in enemies:
    squire_won = battle_engine.do_battle(squire, enemy)
    if not squire_won:
        print("YOU LOSE!")
        exit(0)
    shopping_engine.do_shopping(squire)

print("YOU WIN!")


# 