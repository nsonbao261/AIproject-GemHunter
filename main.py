import sys
from pysat.formula import *
import time
from pysat.solvers import Solver, Minisat22, Glucose3
from algo import *

def generateCnf(matrix):
    solver = Solver(name='mc', use_timer=True)
    for cell in np.argwhere(matrix == "_"):
        solver.add_clause([cellVarible(cell[0], cell[1], matrix), -cellVarible(cell[0], cell[1], matrix)])
    for num in np.argwhere(matrix != "_"):
        var = []
        x, y = int(num[0]), int(num[1])
        adjacentEmptyCells = [item for item in adjacentCells(x, y, matrix) if matrix[int(item[0])][int(item[1])] == "_"]
        for adj in adjacentEmptyCells:
            var.append(cellVarible(adj[0], adj[1], matrix))
        bomb_count = int(matrix[x][y])
        emptyCellCounts = len(var)
        for clauses in getCombination(var, emptyCellCounts - bomb_count + 1):
            solver.add_clause(clauses)
        for clauses in getNegativeCombination(var, bomb_count +1):
            solver.add_clause(clauses)
    return solver




def main(input_file):
    try:
        start_time = time.time()
        arr = createMatrix(input_file)
        pos_arr = np.argwhere(arr != "_")
        solver = generateCnf(arr)
        if(solver.solve()):
            solved_arr = arr
            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if arr[i][j] == "_":
                        var = i*len(arr[0]) + j
                        if(solver.get_model()[var] > 0):
                            solved_arr[i][j] = "B"
                        else:
                            solved_arr[i][j] = "G"
            print(solved_arr)
            array_string = '\n'.join(['\t'.join(map(str, row)) for row in solved_arr])
            with open("output.txt", "w") as file:
                file.write(array_string)
        else:
            print("False")
        end_time = time.time()
        print("Run time: ", end_time - start_time)
    except FileNotFoundError:
        print("Error")

if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Error!")
    main(sys.argv[1])