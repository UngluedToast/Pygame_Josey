import random
import time
def gamestart():
    print("===Graphic design is my passion===")
    print("/\_/\__       __/\_/\       ")
    print("\______\_____/______/       ")
    print("      /.  .  |___________   ")
    print("     (_'_'_)             \> ")
    print("        \ | |________/ | |  ")
    print("        |_|_|        |_|_|  ")
    print("        /_/_|        /_/_|  ")





    print("=======================")
    print("=======greetings=======")
    print("=Please choose a class=")
    print("====== 1. Squire ======")
    print("====== 2. Cleric ======")
    print("=======================")
    choices = [Squire, Cleric]
    # for choice in Player:
    choice = int(input())
        # if choice == 1:
        #     Player = Squire
        # elif choice == 2:
        #     Player = Cleric
    name = input("Please choose a name for you character: ")
    print(name)
    return choices[choice - 1]
    if choices == 0:
        print("A lowley squire, with allegiances to a ruined house, seeking recompense.")
    return(name)




class Character(object):
    def __init__(self):
        self.name = 'undefined'
        self.health = 10
        self.power = 5
        self.coins = 20
        self.evade = 0
        self.armor = 0

    def alive(self):
        return self.health > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        if random.random() < enemy.evade:
            enemy.recieve_damage = False
            print("%s has evaded the attack" % (enemy.name))
        else:
            enemy.receive_damage(self.power)
        time.sleep(1.5)

    def receive_damage(self, points):
        if self.armor >= points:
            print("Your armor deflects the blow in its entirety")
        else:
            self.health -= (points - self.armor)
            print("%s received %d damage." % (self.name, (points - self.armor)))
            if self.armor > 0:
                print("%s aromor deflects some of the blow" % self.name)
        if self.health <= 0:
            print("%s is dead." % self.name)

    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Squire(Character):
    def __init__(self):
        self.name = 'Ser vant'
        self.health = 10
        self.power = 5
        self.coins = 10
        self.evade = 0.1
        self.heal = 0.0
        self.armor = 1
    def restore(self):
        self.health = 10
        print("Squire's heath is restored to %d!" % self.health)
        time.sleep(1)

    def buy(self, item):
        if self.coins >= cost:
            self.coins -= item.cost
            item.apply(squire)
        elif self.coins > cost:
            print("You do not have enough money for that.")

class Cleric(Character):
    def __init__(self):
        self.name = 'Tom'
        self.health = 14
        self.power = 4
        self.coins = 20
        self.evade = 0.05
        self.heal = 0.25
        self.armor = 0
        choose_cleric = "His faith is his shield. Pius and viggillant, he goes forward with his healing gifts"
    def restore(self):
        self.health = 14
        print("Cleric's heath is restored to %d!" % self.health)
        time.sleep(1)
    
    def buy(self, item):
        self.coins -= item.cost
        item.apply(Cleric)

class Shadow(Character):
    def __init__(self):
        self.name = 'Shade'
        self.health = 1
        self.power = 3
        self.evade = 0.9
        self.bounty = 20
        self.armor = 0

class Goblin(Character):
    def __init__(self):
        self.name = 'goblin'
        self.health = 10
        self.power = 2
        self.evade = 0.05
        self.bounty = 4
        self.armor = 1

class Wizard(Character):
    def __init__(self):
        self.name = 'wizard'
        self.health = 8
        self.power = 1
        self.evade = 0.05
        self.bounty = 10
        self.armor = 2

class Swap(Wizard):
    def attack(self, enemy):
        swap_power = random.random() > 0.5
        if swap_power:
            print("%s swaps power with %s during attack" % (self.name, enemy.name))
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power

class Zombie(Character):
    def __init__(self):
        self.name = 'zombie'
        self.health = 20
        self.power = 1
        self.evade = 0.0
        self.bounty = 10
        self.armor = 0

class Bandit(Character):
    def __init__(self):
        self.name = 'bandit'
        self.health = 12
        self.power = 3
        self.evade = 0.25
        self.bounty = 20
        self.armor = 3

class Giant(Character):
    def __init__(self):
        self.name = 'giant'
        self.health = 40
        self.power = 5
        self.evade = 0.0
        self.armor = 3

class Hobgoblin(Character):
    def __init__


class Battle(object):
    def do_battle(self, Squire, enemy):
        print("=====================")
        print("%s faces the %s" % (squire.name, enemy.name))
        print("=====================")
        if enemy.name == Zombie:
            print('You are unsure if you can kill this creature for good yet')
        while squire.alive() and enemy.alive():
            squire.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. flee")
            print("> ",)
            user_input = int(input())
            if user_input == 1:
                squire.attack(enemy)
            elif user_input == 2:
                pass
            elif user_input == 3:
                print("Goodbye.")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
            enemy.attack(squire)
        if squire.alive():
            print("You defeated the %s" % enemy.name)
            time.sleep(1.5)
            print("The %s has dropped %d coins" % (enemy.name, enemy.bounty))
            squire.coins += enemy.bounty
            time.sleep(1.5)
            print("You now have %d coins" % squire.coins)
            return True
        else:
            print("YOU LOSE!")
            return False

class FancyCloak(object):
    cost = 40
    name = "fancy cloak"
    def apply(self, character):
        character.evade += 0.05
        print("%s's evade chance has gone up by 5 percent" % squire.name)

class SuperTonic(object):
    cost = 25
    name = 'super tonic'
    def apply(self, character):
        character.health += 10
        print("%s's health has increased by 10, you now have %d health" % (squire.name, squire.health))

class Armor(object):
    cost = 30
    name = 'armor'
    def apply(self, character):
        character.armor += 2
        print("%s's armor value has incread by two, armor reduces incoming damage by a set amount" % (squire.name))


class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print("%s's health increased to %d." % (character.name, character.health))


class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, character):
        squire.power += 2
        print("%s's power increased to %d." % (squire.name, squire.power))

class Lottery(object):
    cost = 10
    name = 'Lucky Lotto'
    def apply(self, character):
        if random.random() > 0.5:
            squire.coins += 25
            print('good luck you have there, you earned more than double on the chance game.')
        else:
            print('ooh, bad luck, if you play again you can win.')

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword, Armor, SuperTonic, FancyCloak, Lottery]
    def do_shopping(self, squire):
        while True:
            time.sleep(1.5)
            print("=====================")
            print("Welcome to the store!")
            print("=====================")
            print("You have %d coins." % squire.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("10. leave")
            user_input = int(input("> "))
            if user_input == 10:
                break
            else:
                ItemToBuy = Store.items[user_input - 1]
                item = ItemToBuy()
                squire.buy(item)

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
