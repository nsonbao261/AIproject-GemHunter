import numpy as np
from pysat.formula import *
from pysat.solvers import Solver, Minisat22, Glucose3
from itertools import combinations

def getCombination(original_list, number):
    return list(combinations(original_list, number))

def getNegativeCombination(original_list, number):
    allCombinations = combinations(original_list, number)
    return [[-x for x in comb] for comb in allCombinations]

def cellCnf(original_list, number):
    # Generate all possible combinations of indices to place negative values
    index_combinations = combinations(range(len(original_list)), number)

    # Generate lists with exactly two negative values
    result_lists = []
    for indices in index_combinations:
        new_list = original_list.copy()
        for index in indices:
            new_list[index] *= -1
        result_lists.append(new_list)

    return result_lists



def adjacentEmptyCells(x, y, matrix):
    rows = len(matrix[0])
    cols = len(matrix)
    adjacent_cells = []
    for i in range(x-1, x+2):
        if i < 0 or i >= cols:
            continue
        for j in range(y-1, y+2):
            if j < 0 or j >= rows:
                continue
            if i == x and j == y:
                continue 
            if(matrix[i][j] != "_"):
                continue
            adjacent_cells.append((i, j))
    return adjacent_cells


def cellVarible(x, y, matrix):
    return int(x)*len(matrix[0]) + int(y) + 1




def generateCnf(matrix):
    solver = Solver(name='mc')
    for cell in np.argwhere(matrix == "_"):
        solver.add_clause([cellVarible(cell[0], cell[1], matrix), -cellVarible(cell[0], cell[1], matrix)])
    for num in np.argwhere(matrix != "_"):
        var = []
        x, y = int(num[0]), int(num[1])
        for adj in adjacentEmptyCells(x, y, matrix):
            var.append(cellVarible(adj[0], adj[1], matrix))
        bomb_count = int(matrix[x][y])
        emptyCellCounts = len(var)
        for clauses in getCombination(var, emptyCellCounts - bomb_count + 1):
            solver.add_clause(clauses)
        for clauses in getNegativeCombination(var, bomb_count +1):
            solver.add_clause(clauses)
    return solver



def main():
    with open("input.txt") as inputFile:
        lines = [line.rstrip("\n").split(", ") for line in inputFile]
        arr = np.array(lines)
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

if __name__ == "__main__":
    main()