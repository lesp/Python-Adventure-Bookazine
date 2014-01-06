__author__ = 'Les Pounder'

"""
Use compass directions to control movement, and store the POV of the player as a variable
"""

from time import *
from random import *
from time import sleep

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
    HP = randint(5,20)
    MP = randint(5,20)

#We now use our function to
title()
castle()
setup()
global name
global HP
global MP
global move
print "Welcome to the land of Narule" + " " + name
sleep(2)
print "Your health is" + " " + str(HP)
print "Your magic skill is" + " " + str(MP)



print "Would you like to venture out into the land? Press y then enter to continue"
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

north()
east()
west()

if raw_input() == "n":
    print "You move to the north, walking in the sunshine."
elif raw_input() == "e":
    print "You walk to the river which lies to the east of your home."
elif raw_input() == "w":
    print "You walk to the field of wild flowers, stopping to take in the beauty"

