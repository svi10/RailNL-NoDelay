from code.classes.trajectory import Trajectory
from code.classes.trajectories import Trajectories
import csv


def convert_solution(solution):
    """
    Converts the solution from a list into a csv file
    """
    filename = solution.get_file_name('.csv')

    with open (f'solutions/csv_files/{filename}', 'w', newline='') as f:
        writer = csv.writer(f)
        # Write the headers
        writer.writerow(['train', 'stations'])

        # Write the content
        # Write the information of one trajectory per row
        for i in range(len(solution.trajectories)):
            printable = []

            # Create a list that contains all names of the station in a trajectory in the right order
            for station in solution.trajectories[i].stations:
                printable.append(station.name)

            # Ensure the printable has the appropriate format
            # Removes the quotation marks from around the names of the stations
            printable = ('[%s]' % ', '.join(map(str, printable)))

            # Write down the trajectory information in the csv file
            writer.writerow([f'train_{i + 1}', printable])

        # Write the final row containing the quality score
        # If quality has not been determined, this gives the defualt quality value
        writer.writerow(['score', solution.quality])
        