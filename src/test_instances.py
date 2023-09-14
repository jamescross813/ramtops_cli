from player_character import PlayerCharacter
from npc import Npc

new_player = PlayerCharacter("Bob", "male")

print(new_player.name)

new_npc = Npc("Fish", "Fighter", 300, "Cute and fluffy on the outside, but those puppy dog eyes will defeat all")

print(new_npc.name)