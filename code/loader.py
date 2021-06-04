from station import Station
from trajectory import Trajectory

def load_stations(file):
    stations = {}

    with open(stationfile) as f:
        reader = cvs.Reader(f)
        
        for row in reader:
            row["x"] = int(row["x"])
            row["y"] = int(row["y"])
            stations
         

def load_connections(filename):
    connections = {}