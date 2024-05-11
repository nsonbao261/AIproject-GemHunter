from algo import *
import numpy as np
from itertools import product


def checkMatrixValid(matrix):
    numberCells = [(row_index, col_index) for row_index, row in enumerate(matrix) for col_index, col in enumerate(matrix[0]) if (matrix[row_index][col_index] not in ["B", "G"])]
    for cell in numberCells:
        x, y = int(cell[0]), int(cell[1])
        bomb_count = len(getAdjBomb(x, y, matrix))
        if bomb_count != int(matrix[x][y]):
            return False
    return True

def bruteForce(matrix):

    emptyCells = np.argwhere(matrix == "_")

    combinationTuple = list(product(["B", "G"], repeat = len(emptyCells)))
    combinationList = [list(comb) for comb in combinationTuple]

    for item in combinationList:
        for i in range(len(emptyCells)):
            x, y = int(emptyCells[i][0]), int(emptyCells[i][1])
            matrix[x][y] = item[i]
        if checkMatrixValid(matrix):
            return matrix
    
    return None