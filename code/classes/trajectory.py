class Trajectory:
    """
    Class Trajectory is an object that describes connections between the 22 most important train stations.
    """

    def __init__(self):
        self.duration = 0
        self.stations = []

    # def timing(self):
    #     if time > 120:
    #         return False
    #     else:
    #         return True

    def add_station(self, station):
        self.stations.append(station)

    def get_stations(self):
        return self.stations

    def get_duration(self):
        return self.duration()
        