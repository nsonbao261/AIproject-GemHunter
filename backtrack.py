import numpy as np
from algo import *

#If a tiles have the number equal its surrounding empty cells, mark all those cells as bomb
def preBombCheck(matrix):
    numberCells = [(row_index, col_index) for row_index, row in enumerate(matrix) for col_index, col in enumerate(matrix[0]) if (matrix[row_index][col_index] not in ["B", "G", "_"])]
    for num in numberCells:
        x, y = int(num[0]), int(num[1])
        bomb_count = int(matrix[x][y])
        empty_cells = getAdjEmpty(x, y, matrix)
        empty_count = len(empty_cells)
        if bomb_count == empty_count:
            for cell in empty_cells:
                matrix[int(cell[0])][int(cell[1])] = "B"
    return matrix 


def checkBombCondition(x, y, matrix):
    adjNumericCells = getAdjNumeric(x, y, matrix)
    for cell in adjNumericCells:
        pos_x, pos_y = int(cell[0]), int(cell[1])
        bomb_count =  len(getAdjBomb(pos_x, pos_y, matrix))
        empty_count = len(getAdjEmpty(pos_x, pos_y, matrix))
        number = int(matrix[pos_x][pos_y])
        if bomb_count > number:
            return False
    return True


def checkGemCondition(x, y, matrix):
    adjNumericCells = getAdjNumeric(x, y, matrix)
    for cell in adjNumericCells:
        pos_x, pos_y = int(cell[0]), int(cell[1])
        bomb_count =  len(getAdjBomb(pos_x, pos_y, matrix))
        empty_count = len(getAdjEmpty(pos_x, pos_y, matrix))
        number = int(matrix[pos_x][pos_y])
        if bomb_count + empty_count < number:
            print("Number: ", pos_x," ",  pos_y)
            return False
    return True


def backtrack(matrix):
    matrix = preBombCheck(matrix)
    emptyCells = np.argwhere(matrix == "_")
    if(len(emptyCells) == 0):
        return matrix
    x, y = int(emptyCells[0][0]), int(emptyCells[0][1])
    matrix[x][y] = "B"
    #Check Condition
    if checkBombCondition(x,y, matrix):
        if backtrack(matrix) is not None:
            return backtrack(matrix) 
    matrix[x][y] = "G"
    if checkGemCondition(x, y, matrix):
        return backtrack(matrix)
    else:
        return None





            