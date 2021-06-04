from code.trajectory import Trajectory
from code.trajectory import Trajectories
import cv


def give_solution(self, graph):
    """
    An algorithm that gives a solution, without taking anything, such as connections, into account
    """
    stations = []

    for i in graph:
        station = graph[i].keys()
        stations.append(station)
    
    solution = Trajectories()

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
        writer.writerows(solution)
