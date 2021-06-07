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
