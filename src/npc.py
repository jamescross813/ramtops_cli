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
    