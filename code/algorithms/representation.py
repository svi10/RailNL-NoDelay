from code.trajectory import Trajectory
from code.trajectory import Trajectories
import cv


def give_solution(self, graph):
    """
    An algorithm that gives a solution, without taking anything, such as connections, into account
    """

    # Make a list with all available stations
    stations = []

    for i in graph:
        station = graph[i].keys()
        stations.append(station)
    
    # Initialize the solution object
    solution = Trajectories()

    # Create 7 trajects and add them to the trajectories
    # Each traject has five stations
    # Note: the connections between stations are disregarded here
    for i in range(7):
        trajectory = Trajectory()

        for j in range(i, i + 5):
            trajectory.add_station(stations[j])

        solution.add_trajectory(trajectory)

    return solution


def convert_solution(self, solution):
    """
    Converts the solution from a list into a csv file
    """
    with open (solution.csv, newline='') as f:
        writer = csv.writer(f)
        # Write the headers
        writer.writerow('train', 'stations')

        # Write the rows with the trajectories
        writer.writerows(solution)

        # Write the row with the quality
        writer.writerow('score', solution.get_quality)
