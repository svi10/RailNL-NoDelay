from code.classes.trajectory import Trajectory
from code.classes.trajectories import Trajectories

import random


def random_solution_1(trajectories):    
    """
    Gives a random solution for Assignment 1.1
    """

    while not trajectories.check_connections():
        # If the previous solution did not contain all connections, start with an empty list of trajectories
        trajectories.empty()
    
        while len(trajectories.trajectories) < 8:
            # Get reandom starting station
            # station will be the starting station object
            station = random.choice(list(trajectories.connections.keys()))

            # Create the Trajectory
            trajectory = Trajectory()
            
            # Add the starting station to the traject
            trajectory.add_station(station)

            # Add additional stations to the trajectory
            # Stop when the time limit is exceeded
            while trajectory.timing():
                while station not in trajectory.get_stations():
                    station = random.choice(list(station.connections.keys()))       # Change to a station.random_connection() method
                trajectory.add_station(station)

    # If a valid answer has been found, return it
    return trajectories
