import csv
from sys import argv

from code.classes.trajectories import Trajectories
from code.visualisation.convert import convert_solution
from code.visualisation.visualisation import map_solution

import code.algorithms.random as random

from code.algorithms.representation import give_solution

if __name__ == "__main__":
    if len(argv) == 2:
        region = argv[1]
    else:
        print("Usage: python3 trajectories.py 'Holland' OR 'Nationaal'")
        exit(1)

    stationfile = f"data/Stations{region}.csv"
    connectionfile = f"data/Connecties{region}.csv"

    trajectories = Trajectories(stationfile, connectionfile)

    trajectories = random.random_solution_1(trajectories)

    # Acquire solutions
    #   solution = give_solution(trajectories.stations, trajectories) 
    #   solution_csv = convert_solution(solution)
