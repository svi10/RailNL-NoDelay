from code.classes.trajectory import Trajectory
from code.classes.trajectories import Trajectories
import csv


def give_solution(graph, trajectories):
    """
    An algorithm that gives a solution, without taking anything, such as connections, into account
    """

    # Make a list with all available stations
    stations = list(graph.values())


    # Initialize the solution object
    solution = trajectories

    # Create 7 trajects and add them to the trajectories
    # Each traject has five stations
    # Note: the connections between stations are disregarded here
    for i in range(7):
        # Initiate traject object
        trajectory = Trajectory()

        # Fill traject object with stations
        for j in range(0, 4):
            trajectory.add_station(stations[j])

        # Add traject to trajectories
        solution.add_trajectory(trajectory)

    return solution


def convert_solution(solution):
    """
    Converts the solution from a list into a csv file
    """
    with open ('solution_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the headers
        writer.writerow(['train', 'stations'])

        for trajectory in solution.trajectories:
            writer.writerow(['trein', solution.stations])
