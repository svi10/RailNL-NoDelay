import matplotlib.pyplot as plt
import csv

def map_solution(stations):
    """
    map out all trajectories from a specific solution
    """

    # Different colors to plot each trajectory in
    colour = ['green', 'red', 'blue', 'lime', 'orange', 'cyan', 'yellow']

    # Create list of coordinates for all stations
    coordinates = []

    file = open('StationsHolland.csv')
    reader = csv.DictReader(file)
    for row in reader:
        coordinates.append(row)
    file.close()

    # Plot the trajectories
    file = open('example_output.csv')
    reader = csv.DictReader(file)
    i = 0
    for row in reader:
        if row.get('train') == 'score':
            break 

        i = i + 1
        # Get all coordinates
        x_values = []
        y_values = []

        stations = row.get('stations')
        
        stations = stations.strip('[')
        stations = stations.strip(']')
        stations = stations.split(', ')
        
        for i in range(len(stations)):
            current_station = stations[i]
            for j in range(len(coordinates)):
                coordinate = coordinates[j]
                if coordinate.get('station') == current_station:
                    x = float(coordinate.get('x'))
                    x_values.append(x)
                    y = float(coordinate.get('y'))
                    y_values.append(y)
                    break

        plt.plot(x_values, y_values, marker='o')
        plt.axis("off")

    file.close()

    plt.show()
