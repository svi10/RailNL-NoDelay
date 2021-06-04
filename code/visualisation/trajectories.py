import loader

class Trajectories:
    """
    Creates trajectories between train stations within the timewindow
    """

    def __init__(self, stationfile, connectionfile):
        self.duration = 0
        self.stations = []

        

    # def timing(self):
    #     if time > 120:
    #         return False

    def check_station(self):
        """
        Check whether all stations are included in a trajectory.
        """
        pass


if __name__ == "__main__":
    import csv
    import sys

    if len(argv) == 2:
        region = sys.argv[2]
    else:
        print("Usage: python3 trajectories.py 'Holland' OR 'Nationaal'")

    stationfile = f"data/Stations{region}.cvs"
    connectionfile = f"data/Connecties{region}.cvs"

    trajectories = Trajectories(stationfile, connectionfile)
    