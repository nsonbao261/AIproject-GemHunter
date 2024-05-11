import numpy as np
from algo import *

def getAdjBomb(x, y, matrix):
    adj = adjacentCells(x, y, matrix)
    return [pos for pos in adj if matrix[int(pos[0])][int(pos[1])] == "B"]



def getAdjEmpty(x, y, matrix):
    adj = adjacentCells(x, y, matrix)
    return [pos for pos in adj if matrix[int(pos[0])][int(pos[1])] == "_"]



def getAdjNumeric(x, y, matrix):
    adj = adjacentCells(x,y,matrix)
    return [pos for pos in adj if matrix[int(pos[0])][int(pos[1])].isdigit()]


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


def bruteForce(matrix):
    emptyCells = np.argwhere(matrix == "_")
    if(len(emptyCells) == 0):
        return matrix
    x, y = int(emptyCells[0][0]), int(emptyCells[0][1])
    matrix[x][y] = "B"
    #Check Condition
    if checkBombCondition(x,y, matrix):
        if bruteForce(matrix) is not None:
            return bruteForce(matrix) 
    matrix[x][y] = "G"
    if checkGemCondition(x, y, matrix):
        return bruteForce(matrix)
    else:
        return None





            