from pieces import *
from tetris import *


def rotation(piece):
    piece2 = [[0 for i in range(len(piece[0]))] for j in range(len(piece))]
    for x in range(len(piece)):
        for y in range(len(piece)):
            piece2[y][len(piece)-1-x] = piece[x][y]
    return piece2


def mouvement(piece, direction):             # -1 pour gauche et 1 pour droite
    for i in piece:
        for j in i:
            if piece[i][j] > 0:
                npiece = piece[i][j]
    for y in maingrid:
        for x in y:
            if maingrid[y][x] == npiece:
                if iscolision(piece, direction):
                    break
                else:
                    maingrid[y][x] = maingrid[y][x+direction]
                    maingrid[y][x] = 0

''' Pas fini

def iscolision(piece, direction): # -1 pour la gauche et 1 pour la droite
    for y in maingrid:
        for x in y:
            if maingrid[y][x+direction] == 9:
                return True
    return False
'''
