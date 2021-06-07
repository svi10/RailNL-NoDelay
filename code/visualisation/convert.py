from code.classes.trajectory import Trajectory
from code.classes.trajectories import Trajectories
import csv


def convert_solution(solution):
    """
    Converts the solution from a list into a csv file
    """
    with open ('solution_file.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the headers
        writer.writerow(['train', 'stations'])

        # Write the content
        for i in range(len(solution.trajectories)):
            printable = []

            for station in solution.trajectories[i].stations:
                printable.append(station.name)

            writer.writerow([f'train_{i+1}', printable])

        # Add additional bit for quality once we reach part two