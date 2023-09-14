from player_character import PlayerCharacter
from npc import Npc
from location import Location
from item import Item

new_player = PlayerCharacter("Bob", "male")
print(new_player.name)

new_npc = Npc("Fish", "Fighter", 300, "Cute and fluffy on the outside, but those puppy dog eyes will defeat all")
print(new_npc.name)

new_location = Location("Lancre Castle", (0,5), "Castle of the Lancre monarch")
print(new_location.coordinates)

new_item = Item("Bread", "some bread", "health", 1, 15, 1)
print(new_item.name)