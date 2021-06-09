# from code.classes.station import Station
from hashlib import new
from code.classes.trajectory import Trajectory
from code.classes.trajectories import Trajectories

import random
import copy

def quality_solution_2(trajectories):
    """
    Gives a high quality solution for Assignment 1.2
    """

    while len(trajectories.trajectories) < 8:
        # Pick a random station which will be the starting station object. 
        station = random.choice(list(trajectories.stations.values()))
        
        # Create the Trajectory
        trajectory = Trajectory()
        
        # Add the starting station to the traject
        trajectory.add_station(station)

        # Add additional stations to the trajectory and stop when the time limit is exceeded
        
        while trajectory.timing():
            
            new_station = station
            possible_stations = list(station.connections.keys())
            i = 0
            print(trajectory.get_stations())
            
            while new_station.name not in trajectory.get_stations():
                print(i)
                i += 1
                print(new_station.name)
                new_station = random.choice(possible_stations)
                possible_stations.remove(new_station)
                if len(possible_stations) == 0:
                    break

            if len(possible_stations) == 0:
                break

            station = new_station

            trajectory.add_station(new_station)
        
    # Calculate the solution of the solution
    trajectories.calculate_quality()    
