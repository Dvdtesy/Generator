import random
import time
#this is the stats

brains = 0
braun = 0
stamina = 0
wisdom = 0
power = 0
constitution = 0
dexterity = 0
speed = 0

answer = ''

#list of super powers

superPowers = ['Flying', 'Super Strength', 'Telepathy', \
               'Super Speed', 'Can Eat a Lot of Hot Dogs', \
               'Good at Skipping Rope']
#first and last names

superfirstname = ['Wonder', 'Whatta', 'Rabid', 'Incredible', \
                  'Astonishing', 'Decent', 'Stupendous', 'Above-Average' \
                  'That Guy', 'Improbably']
superlastname = ['Boy', 'Man', 'Dingo', 'Beefcake', 'Girl', 'Woman', \
                 'Guy', 'Hero', 'Max', 'Dream', 'Macho Man', 'Stallion']
#intro text

print("Are you ready to create a super hero with the Super Hero Generator 3000?")
print("Enter Y/N:")
answer = input()
answer = answer.upper()
while answer != "Y":
    print("I'm sorry, but you have to choose Y to continue!")
    print("Choose Y/N:")
    answer = input()
    answer = answer.upper()
print("Great, let's get started!")

print("Randomizing name...")

#suspense

for i in range(3):
    print(".........")
    time.sleep(3)

print("(I bet you can't stand the suspense!)")
print("")


#choosing name

superName = random.choice(superfirstname) + " " +random.choice(superlastname)

print("Your Super Hero Name is:")
print(superName)

print("")
print("Now it's time to see what super power you have!")
print("(generating super hero power)")

for i in range(2):
    print("..........")
    time.sleep(3)

print("(nah...you wouldn't like THAT one...)")

for i in range(2):
    print("..........")
    time.sleep(3)

print("(almost there...)")

power = random.choice(superPowers)

print("Your new power is:")
print(power)
print("")

print("Last but not least, let's generate your stats!")
print("Will you be super smart? Super strong? Super Good Looking?")
print("Time to find out!")

for i in range(3):
    print("...........")
    time.sleep(3)

    
brains = random.randint(1, 20)
braun = random.randint(1, 20)
stamina = random.randint(1, 20)
wisdom = random.randint(1, 20)
constitution = random.randint(1, 20)
dexterity = random.randint(1, 20)
speed = random.randint(1, 20)

print("Your new stats are:")
print("")
print("Brains: ", brains)
print("Braun: ", braun)
print("Stamina: ", stamina)
print("Wisdom: ", wisdom)
print("Constitution: ", constitution)
print("Dexterity: ", dexterity)
print("Speed: ", speed)
print("")

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






    
