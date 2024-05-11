import sys
import time
from algo import *
from backtrack import *
from satsolver import *
from brute import *

def main(input_file, method):
    try:
        start_time = time.time()
        arr = createMatrix(input_file)
        if method == "backtrack":
            solved_arr = backtrack(arr)
        elif method == "pysat":
            solved_arr = pysatSolver(arr)
        else:
            solved_arr = bruteForce(arr)
        if solved_arr is not None:
            print("Solution: ")
            print(solved_arr)
            array_string = '\n'.join(['\t'.join(map(str, row)) for row in solved_arr])
            with open("output.txt", "w") as file:
                file.seek(0)
                file.truncate()
                file.write(array_string)
        else:
            print("False")
        end_time = time.time()
        print("Run time: ", end_time - start_time)
    except FileNotFoundError:
        print("Error")

if __name__ == "__main__":
    if(len(sys.argv) != 3):
        print("Error!")
    elif(sys.argv[2] not in ["brute", "pysat", "backtrack"]):
        print("Method not found! Current method: brute, pysat")
    else:
        main(sys.argv[1], sys.argv[2])