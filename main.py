import csv
from sys import argv
from code.classes.trajectories import Trajectories
from code.algorithms.representation import give_solution, convert_solution

if __name__ == "__main__":
    if len(argv) == 2:
        region = argv[1]
    else:
        print("Usage: python3 trajectories.py 'Holland' OR 'Nationaal'")
        exit(1)

    stationfile = f"data/Stations{region}.csv"
    connectionfile = f"data/Connecties{region}.csv"

    trajectories = Trajectories(stationfile, connectionfile)

    connections = trajectories.stations
    

    solution = give_solution(connections, trajectories)       # Adjust this
    solution_csv = convert_solution(solution)
        