from code.classes.station import Station
from code.classes.trajectory import Trajectory
import csv 

def load_stations(stationfile):
    stations = {}

    with open(stationfile) as f:
        reader = csv.DictReader(f)
        for row in reader:
            stations[row['station']] = Station(row['station'])
            # print(stations)
        
        print(stations)

def load_connections(connectionfile):
    connections = {}

    with open(connectionfile) as f:
        reader = csv.DictReader(f)
        # for row in reader:
            # print(row['station1'], row['station2'])
        # for row in reader:
        #     row["x"] = int(row["x"])
        #     row["y"] = int(row["y"])
        #     stations()

