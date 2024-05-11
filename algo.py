import numpy as np
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



def adjacentCells(x, y, matrix):
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
            adjacent_cells.append((i, j))
    return adjacent_cells

def getAdjBomb(x, y, matrix):
    adj = adjacentCells(x, y, matrix)
    return [pos for pos in adj if matrix[int(pos[0])][int(pos[1])] == "B"]



def getAdjEmpty(x, y, matrix):
    adj = adjacentCells(x, y, matrix)
    return [pos for pos in adj if matrix[int(pos[0])][int(pos[1])] == "_"]



def getAdjNumeric(x, y, matrix):
    adj = adjacentCells(x,y,matrix)
    return [pos for pos in adj if matrix[int(pos[0])][int(pos[1])].isdigit()]


def cellVarible(x, y, matrix):
    return int(x)*len(matrix[0]) + int(y) + 1

def createMatrix(input_file):
    with open(input_file) as inputFile:
        lines = [line.rstrip("\n").split(", ") for line in inputFile]
        print(lines)
        return np.array(lines)


def checkMatrixValid(matrix):
    numberCells = [(row_index, col_index) for row_index, row in enumerate(matrix) for col_index, col in enumerate(matrix[0]) if (matrix[row_index][col_index] not in ["B", "G"])]
    for cell in numberCells:
        x, y = int(cell[0]), int(cell[1])
        bomb_count = len(getAdjBomb(x, y, matrix))
        if bomb_count != int(matrix[x][y]):
            return False
    return True