#general non-playable character class
class Npc:
    def __init__(self, name, type, hp, description):
        self.name = name
        self.type = type
        self.hp = hp
        self.description = description
    #needs a location
    #need attack points
    #link to item drop?
    def __repr_(self):
        return "This is {0}, an {1}. {2}. Currently health: {3}".format(self.name, self.type, self.description, self.hp)


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
