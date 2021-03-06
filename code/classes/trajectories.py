from code.loader import load_connections, load_stations

class Trajectories:
    """
    Creates trajectories between train stations within the timewindow
    """
    def __init__(self, stationfile, connectionfile):
        self.duration = 0
        self.trajectories = []
        self.stations = load_stations(stationfile)
        self.connections, self.total_connections = load_connections(connectionfile, self.stations)
        self.quality = 0

    #zet algoritme hier
    def add_trajectory(self, trajectory):
        self.trajectories.append(trajectory)    

    # def check_station(self):
    #     """
    #     Check whether all stations are included in a trajectory. 
    #     """
    #     pass

    # functie voor kwaliteit
    # Hoe te vergelijken dat er een traject is met een zo hoog mogelijke kwaliteit tot nu toe

    def check_connections(self):
        """
        Checks whether all available connections are included in the solution.
        Returns True if all connections are being used, else False.
        """
        # Make an overview of all connections that are being used in the solution thusfar
        used_connections = {}
        for trajectory in self.trajectories:
            for i in range(len(trajectory) - 1):
                if trajectory[i] in used_connections.keys():
                    used_connections[trajectory[i]].append(trajectory[i + 1])
                else:
                    used_connections[trajectory[i]] = trajectory[i + 1]

        # Compare the used connections to all available connections
        if self.connections == used_connections:
            return True
        else:
            return False


    def count_trajectories(self):
        return int(len(self.trajectories))

    def empty(self):
        self.trajectories.clear()

    def get_file_name(self, type):
        filename = 'solution_' + str(self.quality) + type
        return filename

    def calculate_quality(self):
        """
        Calculate the quality of the solution.
        """
        # Count the number of used connections
        # First create a list with all connections that occur in the trajectory
        used_connections = []

        for trajectory in self.trajectories:
            for i in range(1, len(trajectory)):
                connection = [trajectory[i], trajectory[i - 1]]

                if connection and connection.reverse() not in used_connections:
                    used_connections.append(connection)

        p  = len(used_connections) / self.total_connections
        T  = self.count_trajectories()
        Min = self.duration
        
        self.quality = p * 10000 - (T * 100 + Min)

    def get_smallest_stations(self, used_stations):
        """
        Returns a list of all stations with the lowest number of connections.
        i.e. in the beginning it will return all stations with one connection, once those are gone all stations with two connections.
        """
        smallest_stations = []

        # Iterate through all possible stations
        for station in list(self.stations.values()):
            # Check if this station is already being used
            if station in used_stations:
                continue
            # Add the station to the list if the list is empty
            elif not smallest_stations:
                smallest_stations.append(station)
            # Replace the list if the current station has less connections than the stations currently in the list
            elif len(station.connections) < len(smallest_stations[0].connections):
                smallest_stations.clear()
                smallest_stations.append(station)
            # If the current station has as many connections as the stations already in the list, add it
            elif len(station.connections) == len(smallest_stations[0].connections):
                smallest_stations.append(station)

        return smallest_stations
