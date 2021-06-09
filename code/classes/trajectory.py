class Trajectory:
    """
    Class Trajectory is an object that describes connections between the 22 most important train stations.
    """

    def __init__(self):
        self.duration = 0
        self.stations = []

    def timing(self):
        if self.duration > 120:
            return False
        else:
            return True

    def add_station(self, station):
        # Update the duration of the trajectory, only if this is not the starting station
        if len(self.stations) != 0:
            # Retrieve the object of the previous station
            previous_station = self.stations[-1]
            # Retrieve the time it takes to go over this connection
            print(previous_station.connections)
            print(self.stations)
            print(previous_station)
            print(station)
            time = previous_station.connections[station]
            # Update the total duration of the trajectory
            self.duration += time

        # Add the new station to the trajectory
        self.stations.append(station)

    def get_stations(self):
        return self.stations

    def get_duration(self):
        return self.duration()
        