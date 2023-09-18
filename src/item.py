#class describing items in world and on characters
class Item:
    def __init__(self, name, description, type, hitpoints, health, defense):
        self.name = name
        self.description = description
        self.type = type
        self.hitpoints = hitpoints
        self.health = health
        self.defense = defense

    def __repr__(self):
        return "A {0}. {1} Using this will give you: Health {2}, Attack {3}, Defense {4}.".format(self.name, self.description, self.health, self.hitpoints, self.defense)

    #when health item is used can not be used for health again
    def used(self):
        if self.type == 'Health':
            self.health = 0