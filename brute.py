from algo import *
import numpy as np
from itertools import product




def bruteForce(matrix):

    emptyCells = np.argwhere(matrix == "_")

    combinationTuple = list(product(["B", "G"], repeat = len(emptyCells)))
    combinationList = [list(comb) for comb in combinationTuple]

    for item in combinationList:
        for i in range(len(emptyCells)):
            x, y = int(emptyCells[i][0]), int(emptyCells[i][1])
            matrix[x][y] = item[i]
        if checkMatrixValid(matrix) == True:
            return matrix
    
    return None