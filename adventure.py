__author__ = 'Les Pounder'

#The lines below import modules of code into our game, in particular these import time functions to allow us to pause and stop the game, and random provides a method of choosing random numbers or characters.
from time import *
from random import *


#This is a function, we use it to do lots of things and then call it by it's name later on
#To create a function we use "def name():" where name can be anything.

def title():
     print "   __                           _          __                                  "
     print "  / /  ___  __ _  ___ _ __   __| |   ___  / _|   /\  /\___ _ __ ___   ___  ___ "
     print " / /  / _ \/ _` |/ _ \ '_ \ / _` |  / _ \| |_   / /_/ / _ \ '__/ _ \ / _ \/ __|"
     print "/ /__|  __/ (_| |  __/ | | | (_| | | (_) |  _| / __  /  __/ | | (_) |  __/\__ \ "
     print "\____/\___|\__, |\___|_| |_|\__,_|  \___/|_|   \/ /_/ \___|_|  \___/ \___||___/"
def castle():

    print ("*                                 |>>>                    +        ")
    print ("+          *                      |                   *       +")
    print ("                    |>>>      _  _|_  _   *     |>>>		   ")
    print ("           *        |        |;| |;| |;|        |                 *")
    print ("     +          _  _|_  _    \\.    .  /    _  _|_  _       +")
    print (" *             |;|_|;|_|;|    \\: +   /    |;|_|;|_|;|")
    print ("               \\..      /    ||:+++. |    \\.    .  /           *")
    print ("      +         \\.  ,  /     ||:+++  |     \\:  .  /")
    print ("                 ||:+  |_   _ ||_ . _ | _   _||:+  |       *")
    print ("          *      ||+++.|||_|;|_|;|_|;|_|;|_|;||+++ |          +")
    print ("                 ||+++ ||.    .     .      . ||+++.|   *")
    print ("+   *            ||: . ||:.     . .   .  ,   ||:   |               *")
    print ("         *       ||:   ||:  ,     +       .  ||: , |      +")
    print ("  *              ||:   ||:.     +++++      . ||:   |         *")
    print ("     +           ||:   ||.     +++++++  .    ||: . |    +")
    print ("           +     ||: . ||: ,   +++++++ .  .  ||:   |             +")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |        *")
    print ("                 ||: . ||: ,   +++++++ .  .  ||:   |")

def north():
    print "To go north press n then enter"
def east():
    print "To go east press e then enter"
def south():
    print "to go south press s then enter"
def west():
    print "To go west press w then enter"


def setup():
    #global is used to create variables that can be used throughout our game
    global name
    global HP
    global MP
    #Our variable "name" is used to store our name, captured by keyboard input.
    name = raw_input("What is your name warrior? ")
    #randint is a great way of adding some variety to your players statistics.
    HP = randint(5,20)
    MP = randint(5,20)

def villager():
    #This will create a randomly named Villager to interact with
    global npcname
    global response
    #Below is a list, we can store lots of things in a list and then retrieve them later.
    responses = ["Hi", "Are you a hero?", "Are you from this village?", "There has been a dark shadow cast across the village"]
    npcnamechoice = ["Roger", "Dexter", "Sarah", "Susan"]
    #Shuffle will shuffle the list contents into a random order.
    shuffle(npcnamechoice)
    npcname = npcnamechoice[0]
    print "Hello, my name is " + npcname
    shuffle(responses)
    response = responses[0]
    print "Would you like to talk to me? Press y to talk to the villager"
    if raw_input() == "y":
        print response
    else:
        print("Goodbye")

def enemy():
    global enemyHP
    global enemyMP
    global enemyname
    enemyHP = randint(5,20)
    enemyMP = randint(5,20)
    #Below is the enemy's name, perhaps you could change this to a list and then shuffle the list, such as we did for the villager above.
    enemyname = "Ogre"
    print "Suddenly you hear a roar, and from the shadows you see an " + enemyname
    print enemyname
    print "Your enemy has " + " " + str(enemyHP) + " " + "Health Points"
    print "Your enemy has " + " " + str(enemyMP) + " " + "Magic Points"


#We now use our functions in the game code, we call the title, the castle picture and then ask the game to run the setup for our character.
title()
castle()
setup()
global name
global HP
global MP
global move
global enemyHP
print "Welcome to the land of Narule" + " " + name
#Sleep is Python's way of pausing the game for a specified number of seconds
sleep(2)
#Below we are using the helper functions to join a string of text to an integer via the str() helper.
print "Your health is" + " " + str(HP)
print "Your magic skill is" + " " + str(MP)



print "Would you like to venture out into the land? Press y then enter to continue"
#Below we use raw_input to ask for user input, and if it is equal to y, then the code underneath is run.
if raw_input() == "y":
    print "You are in your home, with a roaring fireplace in front of you, above the fire you can see your sword and shield"
    print "Would you like to take your sword and shield? Press y then enter to continue"
    if raw_input() == "y":
        #This is a list, and it can store many items, and to do that we "append" items to the list.
        weapons = []
        weapons.append("sword")
        weapons.append("shield")
        print "You are now carrying your" + " " + weapons[0] + " " + "and your" + " " + weapons[1]
    else:
        print "You choose not to take your weapons"
else:
    print "You stay at home, sat in your favourite chair watching the fire grow colder. The land of Narule no longer has a hero."
    print "Game Over"

print "Armed with your " + weapons[0] + " " + "and " + weapons[1] + " you swing open the door to your home and see a green valley gleaming in the sunshine."
print "In the distance to the north you can see a small village, to the east you can see a river and to the west a field of wild flowers."

#Remember those functions we created at the start of the code? Well here we are using them in the game.
north()
east()
west()
move = raw_input("Where would you like to go? ")
if move == 'n':
    print "You move to the north, walking in the sunshine."
    print "A villager is in your path and greets you"
#elif is short for Else If and it means that if the previous condition is false, to check this condition to see if that is true.
elif move == 'e':
    print "You walk to the river which lies to the east of your home."
    print "A villager is in your path and greets you"
elif move == 'w':
    print "You walk to the field of wild flowers, stopping to take in the beauty"
    print "A villager is in your path and greets you"

villager()
enemy()
sleep(10)

fight = raw_input("Do you wish to fight?" )

if fight == "y":
    while HP > 0:
#This loop will only work while our characters HP is greater than 0.
        hit = randint(0,5)
        print "You swing your sword and cause " + str(hit) + " of damage"
        enemyHP = enemyHP - hit
        print enemyHP
        enemyhit = randint(0,5)
        print "The ogre swings a club at you and causes " + str(enemyhit) + " of damage"
        HP = HP - enemyhit
        print HP
else:
    print "You turn and run away from the ogre"

print "This is where this template ends, this is now YOUR world, build your adventure and share it with the world"

print "   _       _                 _"
print "  /_\   __| |_   _____ _ __ | |_ _   _ _ __ ___"
print " //_\\ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \ "
print "/  _  \ (_| |\ V /  __/ | | | |_| |_| | | |  __/"
print "\_/ \_/\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|"

print "                     _ _"
print "  __ ___      ____ _(_) |_ ___"
print " / _` \ \ /\ / / _` | | __/ __|"
print "| (_| |\ V  V / (_| | | |_\__ \ "
print " \__,_| \_/\_/ \__,_|_|\__|___/"

print " _   _  ___  _   _"
print "| | | |/ _ \| | | |"
print "| |_| | (_) | |_| |"
print " \__, |\___/ \__,_|"
print " |___/"
