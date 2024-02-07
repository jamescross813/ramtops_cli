#general non-playable character class
from location import Location

class Npc:
    def __init__(self, name, type, hp, description, hitPoints):
        self.name = name
        self.type = type
        self.hp = hp
        self.description = description
        self.hitPoints = hitPoints
        #needs a location
        #need attack points

    def __repr_(self):
        return "This is {0}, an {1}. {2}. Currenty health: {3}".format(self.name, self.type, self.description, self.hp)


    #def fight
        #linked to player fight
    #def speak
        #need to provide basic lines for chat to player

#enemies
queen = Npc("Queen of the Elves", "Fighter", 200, "Tall, slim dark-haired woman, wearing a dress of red, white and black, the Queen of the Elves can appear in whatever form she likes, and no stated appearance is definitive. She wears a copper crown in her hair and has exquisitely thin hands",)
vampire = Npc("Vlad de Magpyr", "Fighter", 200, "A clever, powerful vampire")
frost_guy = Npc("Wintersmith", "Fighter", 150, "The creator of winter")
boggart = Npc("River Boggart", "Fighter", 75, "A waterbased creature ready to eat the young and weak who linger on the shore.")
hiver = Npc("The Hiver", "Fighter", 200, "A parasite, it takes over the mind and body of other creatures")
#allies
granny = Npc("Granny Weatherwax", "Ally", 250, "Tall, thin with a wart-free complexion and good teeth, (despite her best efforts,) and perpetual scowl")
nanny = Npc("Nanny Ogg", "Ally", 225, "A dumpy and bandy-legged old woman with a face like an apple that's been left too long and an expression of near-terminal good nature")
magrat = Npc("Magrat Garlik", "Ally", 200, "Thin, with a frequently red nose and an unruly mass of frizz and split ends")
tiffany = Npc("Tiffany Aching", "Ally", 150, "Short, slim, brown-haired, wears big boots. Almost never wears black (except for the hat) preferring blue or green")