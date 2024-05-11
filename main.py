import sys
import time
from algo import *
from brute import *
from satsolver import *

def main(input_file, method):
    try:
        start_time = time.time()
        arr = createMatrix(input_file)
        if method == "brute":
            solved_arr = bruteForce(arr)
        else:
            solved_arr = pysatSolver(arr)
        if len(solved_arr) > 0:
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
    elif(sys.argv[2] not in ["brute", "pysat"]):
        print("Method not found! Current method: brute, pysat")
    else:
        main(sys.argv[1], sys.argv[2])