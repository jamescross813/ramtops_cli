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
        
    #moves cutomer south/north/east/west given input
    def north(self):
        current_location = self.coordinates
        self.coordinates[0] = current_location[0]+1
        return self.coordinates
    
    def south(self):
        current_location = self.coordinates
        self.coordinates[0] = current_location[0]-1
        return self.coordinates
    
    def west(self):
        current_location = self.coordinates
        self.coordinates[1] = current_location[1]-1
        return self.coordinates
    
    def east(self):
        current_location = self.coordinates
        self.coordinates[1] = current_location[1]+1
        return self.coordinates
    

    #could include number of 'miles' to move in given direction
    #could include more options for movement (NNW etc) - do with additional coodrinates
    #need check in input stage that direction input is valid
    #quick travel option - do when additional locations.
    #need to search in location db for when info on where character is

loc1 = Location("Mad Stoat", (1,2), "a place")
loc2 = Location("Lancre", (2,3), "a place")
loc3 = Location("Bad Ass", (2,2), "a place")
loc4 = Location("Razor Back", (3,2), "a place")
loc5 = Location("Ramtops", (3,1), "a place")

loc6 = Location("Ramtops", (1,1), "Turn back")
loc7 = Location("Ramtops", (1,3), "Turn back")
loc8 = Location("Ramtops", (1,2), "Turn back")
loc9 = Location("Ramtops", (3,3), "Turn back")