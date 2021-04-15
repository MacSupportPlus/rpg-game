# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee
class Character: 
    def __init__(self, character_health, character_power):
        self.character_health = character_health
        self.character_power = character_power

    def attack(self, character_health):
        self.character_health -= self.character_power
        print("You do {} damage to the opponent.".format(self.character_power))

    def alive(self):
        if self.character_health > 0:
            print('You are alive keep playing')
            return self.character_health
        else:
            print(f"{Character} is Dead {character} Lose")

    def print_status(self):
        print("I have {} health and {} power.".format(self.character_health, self.character_power))

    
class Hero(Character):
    def characterType(self):
        print("I am a hero")


class Goblin(Character): 
    def characterType(self):
        print("I am a goblin!!")

class Zombie(Character): 
    def characterType(self):
        print("I am a zombie")

superHero = Hero(10, 5)
greenGoblin = Goblin(6,2)
DonaldTrump = Zombie(1000000000, 1)


while greenGoblin.alive() > 0 and superHero.alive() > 0:
    superHero.characterType()
    superHero.print_status() 
    greenGoblin.characterType()
    greenGoblin.print_status()
    
    print()
    print("What do you want to do?")
    print("1. fight goblin")
    print("2. do nothing")
    print("3. flee")
    print("> ", end=' ')
    raw_input = input()
    if raw_input == "1":
        # Hero attacks goblin
        superHero.attack(greenGoblin)
        if greenGoblin.character_health <= 0:
            print("The goblin is dead.")
    elif raw_input == "2":
        pass
    elif raw_input == "3":
        print("Goodbye.")
        break
    else:
        print("Invalid input {}".format(raw_input))

    if greenGoblin.character_health > 0:
        # Goblin attacks hero
        greenGoblin.attack(superHero)
        if superHero.character_health <= 0:
            print("You are dead.")

