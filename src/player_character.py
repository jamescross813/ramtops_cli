#player class for playable characters
class PlayerCharacter:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hp = 100
    
    def __repr__(self):
        return "I am {0}, a {1}. My journey through the ramptops has left me with {2} health".format(self.name, self.gender, self.hp)

    #def move

    #def fight

    #def heal

    #def speak

    #def investigate
