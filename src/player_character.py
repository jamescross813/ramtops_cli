#player class for playable characters
class PlayerCharacter:
    def __innit__(self, name, gender):
        self.name = name
        self.gender = gender
        self.hp = 100
