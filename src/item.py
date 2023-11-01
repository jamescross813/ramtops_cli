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
        #should this be changed to just losing item?

bread = Item("Bread", "Some bread.", "Health", 1, 15, 1)
knife = Item("Knife", "A normal kitchen knife.", "Attack", 10, 0, 2)
sword = Item("Sword of Anoia", "A sword forged in the drawers of Anoia.", "Attack", 20, 0, 5)
shield = Item("Shield of Hiding", "A sheild big enough to hide behind.", "Defense", 0, 0, 20)
frying_pan =Item("Frying Pan", "A cast iron fryign pan.", "Attack", 15, 0, 2)
hat = Item("Witch's Hat", "A black pointy hat", "Defense", 2, 0, 5)
potion = Item("Health Potion", "A delicious smelling poition", "Health", 0, 25, 0)