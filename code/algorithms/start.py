import cv



def give_solution(self, graph):
    """
    An algorithm that gives a solution, without taking anything, such as connections, into account
    """
    

def convert_solution(self, solution):
    """
    Converts the solution from a list into a csv file
    """
    with open (solution.csv, newline='') as f:
        writer = csv.writer(f)
        writer.writerows(solution)
