# from code.classes.station import Station
from code.classes.trajectories import Trajectories

import random

def quality_solution_2(trajectories, quality):
    """
    Gives a high quality solution for Assignment 1.2
    """

    while not quality.scipy.optimize.maximize():
        # If the previous solution did not contain maximize quality 'K', start with an empty list of trajectories
        trajectories.empty()
    
        while trajectories.count_trajectories < 8:
            # Pick a random station which will be the starting station object. All following connections will form a list where each connection looks like [station, distance]
            station = random.choice(list(trajectories.connections.keys()))

            # Create the Trajectory
            trajectory = Trajectory()
            
            # Add the starting station to the traject
            trajectory.add_station(station)

            # Add additional stations to the trajectory and stop when the time limit is exceeded
            while trajectory.timing:
                while station not in trajectory.get_stations():
                    station = random.choice(list(station.connections.keys()))
                trajectory.add_station(station)
            
            # Calculate a trajectory's quality
            p = ((trajectories.count_trajectories)/list.count(Trajectories.connections.keys()))
            T = trajectories.count_trajectories
            Min = trajectory.timing
            quality = p *10000 - (T * 100 + Min)

            # Save the trajectory only if the quality is maximized
            if quality.scipy.optimize.maximize():
                return quality