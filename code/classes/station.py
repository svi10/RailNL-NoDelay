# from data import csv

class Station:
    """
    Class Station is an object that describes a single station. 
    """
    def __init__(self, name, x, y):

        # initializes station properties
        self.name = name
        self.x = x
        self.y = y
        self.connections = {}
        # "key: connectedstation";"value: tripduration"
        
        # sets attribute visited equal to false when the station is first initialized
        self.visited = False

    def __repr__(self):
        return self.name

    def add_connection(self, destination, tripduration):
        """
        Accepts another Station (object) and tripduration, and stores those in the dictionary
        """
        self.connections[destination] = tripduration
    
    def has_connection(self, destination):
        """
        Accepts a connection, and checks whether there is a connection in the dictionary
        """
        if destination in self.connections.keys():
            return True
        else:
            return False

    # Weten niet zeker of een station accept hoeft te worden, omdat dat het sws al doet. Het gaat om de tijd. Tijd key??
    def get_connection(self, tripduration):
        """
        Accepts a destination, and retrieves the actual Tripduration that it takes
        """
        return self.connections[tripduration]

    def set_visited(self):
        """
        adds the current station to the list of visited stations
        """
        self.visited = True

    # def already_visited(self):
    #     """
    #     returns true if you visited a stations already else return false
    #     """
    #     if self.visited is True:
    #         return True
    #     else:
    #         return False