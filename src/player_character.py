#player class for playable characters
class PlayerCharacter:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hp = 100
    
    def __repr__(self):
        return "I am {0}, a {1}. My journey through the ramptops has left me with {2} health".format(self.name, self.gender, self.hp)

    def movement(self):
        pass
        #input of direction (NESW)
        #swtich staement to cthrow to appropriate location method

    #def fight
        #allow choice of weapon or fist (default attack value 2)
        #while loop to check health values of player and enemy

    #def heal
        #use health object to heal health
        #throw to item to use up health item

    #def speak
        #input from user?

    #def investigate
        #find items in certain locations, items will need location attr
        #throw to location, which will throw to item?- location will check with item if items db has anything at given location?