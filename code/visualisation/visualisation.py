import matplotlib.pyplot as plt
import csv

from code.classes.station import Station


def map_solution(solution, trajectories):
    """
    map out all trajectories from a specific solution
    """

    # Different colors to plot each trajectory in
    colors = ['green', 'red', 'blue', 'lime', 'orange', 'cyan', 'yellow']

    # Plot the trajectories
    plt.figure(figsize=(10,10))
    
    file = open(solution)
    reader = csv.DictReader(file)

    # Initialize counter
    c = 0

    for row in reader:
        # End when the end of the file is reached
        if row.get('train') == 'score':                 
            score = row.get('stations')
            break 

        # Retrieve all stations in the trajectory
        stations = row.get('stations')
        
        # Clean up the list of stations
        stations = stations.strip('[]').split(', ')

        # Get coordinates for each train in the trajectory
        x_values = []
        y_values = []

        for station_name in stations:
            # Acquire the station object
            station = trajectories.stations[station_name]

            # Save the coordinates
            x_values.append(float(station.x))
            y_values.append(float(station.y))
            
            # Add the name of the station to the point in the plot
            plt.annotate(station.name, (station.x, station.y))                 

        plt.plot(x_values, y_values, marker='o', color=colors[c], label=f'train {c+1}')
        plt.axis("off")

        # Update counter
        c = c + 1

    file.close()

    # Plot the figure
    plt.legend()
    plt.title(f'score = {score}')
    plt.savefig('solutions/solution.png')
    plt.show()
