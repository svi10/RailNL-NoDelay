from code.loader import load_connections, load_stations

class Trajectories:
    """
    Creates trajectories between train stations within the timewindow
    """
    def __init__(self, stationfile, connectionfile):
        self.duration = 0
        self.trajectories = []
        self.stations = load_stations(stationfile)
        self.connections = load_connections(connectionfile, self.stations)

    #zet algoritme hier
    def add_trajectory(self, trajectory):
        self.trajectories.append(trajectory)    

    # def check_station(self):
    #     """
    #     Check whether all stations are included in a trajectory. 
    #     """
    #     pass

    # functie voor kwaliteit

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
        return int(len(trajectories))

    def empty(self):
        self.trajectories.clear()
