#import player, npc, item, location
from location import Location
from player_character import PlayerCharacter
from npc import Npc
from item import Item

import click

class Cli:
    @click.command()
    @click.option("--name", prompt="Welcome to the Ramptops! We're happy to have you here, but what's your name traveller?", help="The name of the user")
    
    def hello(name):
        click.echo(f"Hello {name}!")
        
    hello()

#ask what player wants to do
#check input is allowed
#send to appropriate function(swtich statement)
#if location changes, check for items and enemies--> give choice to pick up/fight respectively
