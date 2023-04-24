from pieces import *
from tetris import maingrid

def rotate_piece(piece):

    piece2 = [[0 for x in range(len(piece))] for y in range(len(piece[0]))]
    for x in range(len(piece[0])):
        for y in range(len(piece)):
            piece2[x][y] = piece[len(piece) - y - 1][x]
    piece = piece2
    return piece


# Testé et fonctionnel
def poser(piece, x, y):
    global piece_x, piece_y
    piece_x, piece_y = x, y
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] != 0:
                maingrid[i+y][j+x+1] = piece[i][j]
                


def collision(piece):
    global maingrid, piece_x, piece_y
    for y in range(len(piece)):
        for x in range(len(piece)):
            if piece[y][x] != 0:
                if maingrid[piece_y + y][piece_x + x + 1] != 0:
                    return True
    return False


def destroyline():
    global score, level, completedlines, totallines
    completedlines = 0
    destroyed = False


    for y in range(len(maingrid)-3):
        if all(maingrid[y]):
            maingrid.pop(y)
            maingrid.insert(0, [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8])
            completedlines += 1
            totallines += 1
            destroyed = True

    if destroyed:
        score += ((100 + 200 * (completedlines - 1)) * level)
