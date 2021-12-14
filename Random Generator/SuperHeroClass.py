import random
import time


class Superhero():
    def __init__(self):
        self.superName = superName
        self.power = power
        self.braun = braun
        self.brains = brains
        self.stamina = stamina
        self.wisdom = wisdom
        self.constitution = constitution
        self.dexterity = dexterity
        self.speed = speed

braun = random.randint(1, 20)
brains = random.randint(1, 20)
stamina = random.randint(1, 20)
wisdom = random.randint(1, 20)
constitution = random.randint(1, 20)
dexterity = random.randint(1, 20)
speed = random.randint(1, 20)

superPowers = ['Flying', 'Super Strength', 'Telepathy', 'Super Speed', \
               'Can Eat a Lot of Hot Dogs', 'Good at Skipping Rope']

power = random.choice(superPowers)

superFirstName = ['Wonder', 'Whatta', 'Rabid', 'Incredible', \
                  'Astonishing', 'Decent', 'Stupendous', 'Above-Average' \
                  'That Guy', 'Improbably']

superLastName = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', \
                 'Guy', 'Hero', 'Max', 'Dream', 'Macho Man', 'Stallion']

superName = random.choice(superFirstName)+ " " +random.choice(superLastName)

class Mutate(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a Mutate!")
        self.speed = self.speed + 10

class Robot(Superhero):
    def __init__(self):
        Superhero.__init__(self)
        print("You created a robot!")
        self.braun = self.braun + 10

#intro text

print("Are you ready to create a super hero with the Super Hero Generator 3000?")
print("Enter Y/N:")

answer = input()
answer = (answer.upper())

while answer != "Y":
    print("I'm sorry, but you have to choose Y to continue!")
    print("Enter Y/N:")
    answer = input()
    answer = (answer.upper())

print("Great, let's get started!")

print("Choose from the following hero options: ")
print("Press 1 for a Regular Superhero")
print("Press 2 for a Mutate Superhero")
print("Press 3 for a Robot Superhero")
answer2 = input()

if answer2=='1':
    hero = Superhero()
    print("You created a regular super hero!")
    print("Generating stats, name, and super powers.")
    
    for i in range(1):
        print("...........")
        time.sleep(3)

        print("(nah...you wouldn't like THAT one...)")

    for i in range(2):
        print("...........")
        time.sleep(3)

    print("(almost there...)")
    print(" ")
    print("Your name is %s." % (hero.superName))
    print("Your new power is: ", hero.power)
    print("Your new stats are:")
    print("")
    print("Brains: ", hero.brains)
    print("Braun: ", hero.braun)
    print("Stamina: ", hero.stamina)
    print("Wisdom: ", hero.wisdom)
    print("Constitution: ", hero.constitution)
    print("Dexterity: ", hero.dexterity)
    print("Speed: ", hero.speed)
    print("")

elif answer2=='2':
    hero2 = Mutate()
    print("Generating stats, name, and super powers.")
    
    for i in range(1):
        print("...........")
        time.sleep(3)

        print("(nah...you wouldn't like THAT one...)")

    for i in range(2):
        print("...........")
        time.sleep(3)
        
    print("Your new name is %s." % (hero2.superName))
    print("Your new power is: ", hero2.power)
    print("Your new stats are:")
    print("")
    print("Brains: ", hero2.brains)
    print("Braun: ", hero2.braun)
    print("Stamina: ", hero2.stamina)
    print("Wisdom: ", hero2.wisdom)
    print("Constitution: ", hero2.constitution)
    print("Dexterity: ", hero2.dexterity)
    print("Speed: ", hero2.speed)
    print("")
    print("Please enter your super hero name: ")

elif answer2=='3':
    hero3 = Robot()

    print("Generating stats, name, and super powers.")

    for i in range(1):
        print("...........")
        time.sleep(3)

        print("(nah...you wouldn't like THAT one...)")

    for i in range(2):
        print("...........")
        time.sleep(3)

    print("Your new name is %s." % (hero3.superName))
    print("Your new power is: ", hero3.power)
    print("Your new stats are:")
    print("")
    print("Brains: ", hero3.brains)
    print("Braun: ", hero3.braun)
    print("Stamina: ", hero3.stamina)
    print("Wisdom: ", hero3.wisdom)
    print("Constitution: ", hero3.constitution)
    print("Dexterity: ", hero3.dexterity)
    print("Speed: ", hero3.speed)
    print("")

else:
    print("You did not choose the proper answer! Program will now self-destruct!")

print("Here is a summary of your new Super Hero!")
print("Thanks for using the Super Hero Generator 3000!")
print("Tell all your friends!")
print("")
print("Character Summary")
print("")
print("")
print("Super Hero Name: ", superName)
print("Super Power: ", power)
print("")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
print(" ")


print("Would you like to start over and create a new hero?")
print("Enter Y/N:")
answer3 = input()
answer3 = (answer.upper())
if answer3 == "N":
    print("Goodbye!")
if answer3 == "Y":
    print(" ")
    print("Great, let's get started!")

    print("Choose from the following hero options: ")
    print("Press 1 for a Regular Superhero")
    print("Press 2 for a Mutate Superhero")
    print("Press 3 for a Robot Superhero")
    print(" ")
    answer2 = input()

    if answer2=='1':
        hero = Superhero()
        print("You created a regular super hero!")
        print("Generating stats, name, and super powers.")
        
        for i in range(1):
            print("...........")
            time.sleep(3)

            print("(nah...you wouldn't like THAT one...)")

        for i in range(2):
            print("...........")
            time.sleep(3)

        print("(almost there...)")
        print(" ")
        print("Your name is %s." % (hero.superName))
        print("Your new power is: ", hero.power)
        print("Your new stats are:")
        print("")
        print("Brains: ", hero.brains)
        print("Braun: ", hero.braun)
        print("Stamina: ", hero.stamina)
        print("Wisdom: ", hero.wisdom)
        print("Constitution: ", hero.constitution)
        print("Dexterity: ", hero.dexterity)
        print("Speed: ", hero.speed)
        print("")

    elif answer2=='2':
        hero2 = Mutate()
        print("Generating stats, name, and super powers.")
        
        for i in range(1):
            print("...........")
            time.sleep(3)

            print("(nah...you wouldn't like THAT one...)")

        for i in range(2):
            print("...........")
            time.sleep(3)
            
        print("Your new name is %s." % (hero2.superName))
        print("Your new power is: ", hero2.power)
        print("Your new stats are:")
        print("")
        print("Brains: ", hero2.brains)
        print("Braun: ", hero2.braun)
        print("Stamina: ", hero2.stamina)
        print("Wisdom: ", hero2.wisdom)
        print("Constitution: ", hero2.constitution)
        print("Dexterity: ", hero2.dexterity)
        print("Speed: ", hero2.speed)
        print("")
        print("Please enter your super hero name: ")

    elif answer2=='3':
        hero3 = Robot()

        print("Generating stats, name, and super powers.")

        for i in range(1):
            print("...........")
            time.sleep(3)

            print("(nah...you wouldn't like THAT one...)")

        for i in range(2):
            print("...........")
            time.sleep(3)

        print("Your new name is %s." % (hero3.superName))
        print("Your new power is: ", hero3.power)
        print("Your new stats are:")
        print("")
        print("Brains: ", hero3.brains)
        print("Braun: ", hero3.braun)
        print("Stamina: ", hero3.stamina)
        print("Wisdom: ", hero3.wisdom)
        print("Constitution: ", hero3.constitution)
        print("Dexterity: ", hero3.dexterity)
        print("Speed: ", hero3.speed)
        print("")

    else:
        print("You did not choose the proper answer! Program will now self-destruct!")

    print("Here is a summary of your new Super Hero!")
    print("Thanks for using the Super Hero Generator 3000!")
    print("Tell all your friends!")
    print("")
    print("Character Summary")
    print("")
    print("")
    print("Super Hero Name: ", superName)
    print("Super Power: ", power)
    print("")
    print("Brains: ", brains)
    print("Braun: ", braun)
    print("Stamina: ", stamina)
    print("Wisdom: ", wisdom)
    print("Constitution: ", constitution)
    print("Dexterity: ", dexterity)
    print("Speed: ", speed)
    print(" ")

    repsonse = input("Pick teams again? Type y or n: ")

