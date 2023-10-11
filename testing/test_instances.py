from src.npc import Npc
from src.location import Location
from src.item import Item
from src.player_character import PlayerCharacter

new_player = PlayerCharacter("Bob", "male")
print(new_player)

new_npc = Npc("Fish", "Fighter", 300, "Cute and fluffy on the outside, but those puppy dog eyes will defeat all")
print(new_npc.name)

new_location = Location("Lancre Castle", [0,5], "Castle of the Lancre monarch")
print(new_location.coordinates)

new_item = Item("Bread", "some bread", "health", 1, 15, 1)
print(new_item.name)