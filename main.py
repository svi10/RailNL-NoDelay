import csv
from sys import argv

from code.classes.trajectories import Trajectories
from code.visualisation.convert import convert_solution
from code.visualisation.visualisation import map_solution

import code.algorithms.random as random

from code.algorithms.representation import give_solution
from code.algorithms.randomquality import quality_solution_2

if __name__ == "__main__":
    if len(argv) == 2:
        region = argv[1]
    else:
        print("Usage: python3 trajectories.py 'Holland' OR 'Nationaal'")
        exit(1)

    stationfile = f"data/Stations{region}.csv"
    connectionfile = f"data/Connecties{region}.csv"

    trajectories = Trajectories(stationfile, connectionfile)
    
    quality_solution_2(trajectories)

    print(trajectories.quality)

   
"""
    # Acquire solutions
    give_solution(trajectories.stations, trajectories) 
    convert_solution(trajectories)

    solution_csv = trajectories.get_file_name('.csv')
    map_solution(f'solutions/csv_files/{solution_csv}', trajectories)
"""
