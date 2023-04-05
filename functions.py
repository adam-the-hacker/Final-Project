from pieces import *
from tetris import maingrid

# Testé et fonctionnel
def rotate_piece(piece, n):
    for i in range(n % 4):
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
            maingrid[i+y][j+x+1] = piece[i][j]
            
# Testé et fonctionnel
def deplacer_piece(piece, x, y):
    global piece_x, piece_y, rotated_bloc
    npiece = 0
    for z in range(len(piece)):
        for v in range(len(piece[0])):
            if piece[z][v] != 0:
                npiece = piece[z][v]

    piece = rotate_piece(piece, (rotated_bloc % 4) - 1)

    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == npiece:
                maingrid[i + piece_y][j + piece_x + 1] = 0

    piece = rotate_piece(piece, 1)

    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == npiece:
                maingrid[i + piece_y][j + piece_x + 1] = 0

    piece_x, piece_y = x, y
    poser(piece, x, y)


# Testé et fonctionnel 
def randombloc():
    global activebloc
    activebloc = bloc = choice([cyan, blue, orange, yellow, green, purple, red])
    return bloc
# Utiliser poser(randombloc(), x, y) pour générer un bloc aléatoire

