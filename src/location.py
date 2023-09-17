#class for locations on map
class Location:
    def __init__(self, name, coordinates, description):
        self.name = name
        self.coordinates = coordinates
        self.description = description
        
    def __repr__(self):
        return "Welcome to {0}, {2}. Your current coordinates are {2}".format(self.name, self.description, self.coordinates)