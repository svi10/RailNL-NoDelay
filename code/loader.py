from code.classes.station import Station
from code.classes.trajectory import Trajectory
import csv 

def load_stations(stationfile):
    stations = {}

    with open(stationfile) as f:
        reader = csv.DictReader(f)
        for row in reader:
            stations[row['station']] = Station(row['station'], float(row['x']), float(row['y']))
            
    return stations    

def load_connections(connectionfile, stations):
    # Initialize a general overview of all connections
    connections = {}
    
    with open(connectionfile) as connection_file:
        reader = csv.DictReader(connection_file)
        for row in reader:
            # Add connections to the station object
            stations[row['station1']].add_connection(stations[row['station2']], int(row['distance']))
            stations[row['station2']].add_connection(stations[row['station1']], int(row['distance']))

            # Add connections to general overview
            update_overview(connections, row['station1'], row['station2'])
            update_overview(connections, row['station2'], row['station1'])

    return connections

def update_overview(overview, station_1, station_2):
    if station_1 in overview:
        overview[station_1].append(station_2)
    else:
        overview[station_1] = [station_2]
    