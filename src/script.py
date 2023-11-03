#import player, npc, item, location
from location import Location
from player_character import PlayerCharacter
from npc import Npc
from item import Item

import click

class Cli:
    def welcome():
        name = input("Welcome to the Ramptops! We're happy to have you here, but what's your name traveller?")
        Cli.hello(name)
    
    def hello(name):
        print(f"Welcome {name}")

 
        
Cli.welcome()

    
#ask what player wants to do
#check input is allowed
#send to appropriate function(swtich statement)
#if location changes, check for items and enemies--> give choice to pick up/fight respectively
