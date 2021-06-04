import matplotlib.pyplot as plt
import csv

def map_solution(solution):
    """
    map out all trajectories from a specific solution
    """

    # Different colors to plot each trajectory in
    colors = ['green', 'red', 'blue', 'lime', 'orange', 'cyan', 'yellow']

    # Create list of coordinates for all stations
    coordinates = []

    file = open('StationsHolland.csv')  # ! Adjust this so the file can be varied based on the user input
    reader = csv.DictReader(file)
    
    for row in reader:
        coordinates.append(row)
    file.close()

    # Plot the trajectories
    plt.figure(figsize=(10,10))
    
    file = open(solution)
    reader = csv.DictReader(file)

    # Initialize counter
    c = 0

    for row in reader:
        # End when the end of the file is reached
        if row.get('train') == 'score':
            break 

        # Retrieve all stations in the trajectory
        stations = row.get('stations')
        
        # Clean up the list of stations
        stations = stations.strip('[]').split(', ')
        

        # Get coordinates for each train in the trajectory
        x_values = []
        y_values = []

        for i in range(len(stations)):
            current_station = stations[i]
            for j in range(len(coordinates)):
                coordinate = coordinates[j]
                if coordinate.get('station') == current_station:
                    x = float(coordinate.get('x'))
                    x_values.append(x)

                    y = float(coordinate.get('y'))
                    y_values.append(y)

                    # Add the name of the station to the point in the plot
                    plt.annotate(current_station, (x, y))

                    break

        plt.plot(x_values, y_values, marker='o', color=colors[c], label=f'train {c+1}')
        plt.axis("off")

        # Update counter
        c = c + 1

    file.close()

    # Plot the figure
    plt.legend()
    plt.show()

# Render example output 
map_solution('example_output.csv')
