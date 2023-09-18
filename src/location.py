#class for locations on map
class Location:
    def __init__(self, name, coordinates, description):
        self.name = name
        self.coordinates = coordinates
        self.description = description
        
    def __repr__(self):
        return "Welcome to {0}, {2}. Your current coordinates are {2}".format(self.name, self.description, self.coordinates)
    
    def locate_player(self):
        return "{0}: {1}".format(self.name, self.coordinates)
    
    def north(self):
        current_location = self.coordinates
        self.coordinates[0] = current_location[0]+1
        return self.coordinates
    
    def south(self):
        current_location = self.coordinates
        self.coordinates[0] = current_location[0]-1
        return self.coordinates
    
    