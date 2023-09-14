#class describing items in world and on characters
class Item:
    def __init__(self, name, description, type, hitpoints, health, defense):
        self.name = name
        self.description = description
        self.type = type
        self.hitpoints = hitpoints
        self.health = health
        self.defense = defense

    #def __repr__()