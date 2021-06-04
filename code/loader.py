from code.classes.station import Station
from code.classes.trajectory import Trajectory
import csv 

def load_stations(stationfile):
    stations = {}

    with open(stationfile) as f:
        reader = csv.DictReader(f)
        for row in reader:
            stations[row['station']] = Station(row['station'])

    return stations    
        # print(stations)

def load_connections(connectionfile, stations):
    connections = {}
    
    with open(connectionfile) as connection_file:
        reader = csv.DictReader(connection_file)
        for row in reader:
            stations[row['station1']].add_connection(stations[row['station2']], int(row['distance']))
            stations[row['station2']].add_connection(stations[row['station1']], int(row['distance']))

    return 
            # if stations[row['station1']] in connections.keys():
                # connections[stations[row['station1']]] = stations[row['station2']], int(row['distance'])
            # connections[stations[row['station2']]] = connections[row['station1']], connections[row['distance']]

            # connections[row['station1']] = stations[row['station1']]
            
            
        # print(connections)
            # row['station2'])
