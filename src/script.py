#import player, npc, item, location
from location import Location
from player_character import PlayerCharacter
from npc import Npc
from item import Item

import click

class Cli:
    temp_loc ={}
    def welcome():
        name = input("Welcome to the Ramptops! We're happy to have you here, but what's your name traveller?")
        Cli.hello(name)
    
    def hello(name):
        print(f"Welcome {name}")

    #def check- where you are- check for allies and enemies and items--> give appropriate options

    def check():
        location = PlayerCharacter.current_location()
        if PlayerCharacter.current_location() == False:
            temp_loc ={0,0}
        else:
            Location.__repr__()
        Cli.checkLocation(location)
        
    
    def checkLocation(location):
        #check location for allies/enemies
            #if present let player know/give option to interact/fight
        #check location for items
            #if present let player interCact

    #def options: what do you want to do

    

# Cli.welcome()

    
#ask what player wants to do
#check input is allowed
#send to appropriate function(swtich statement)
#if location changes, check for items and enemies--> give choice to pick up/fight respectively
