from pieces import *
from tetris import maingrid

# Testé et fonctionnel
def rotation(piece):
    piece2 = [[0 for i in range(len(piece))] for j in range(len(piece[0]))]
    for x in range(len(piece)):
        for y in range(len(piece[0])):
            piece2[y][len(piece) - 1 - x] = piece[x][y]
    return piece2

# Testé et fonctionnel
def poser(piece, x, y):
    global piece_x, piece_y
    piece_x, piece_y = x, y
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            maingrid[i+y][j+x+1] = piece[i][j]
            
# Testé et fonctionnel
def deplacer_piece(piece, x, y):
    global piece_x, piece_y
    npiece = 0
    for z in range(len(piece)):
        for v in range(len(piece[0])):
            if piece[z][v] != 0:
                npiece = piece[z][v]
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] == npiece:
                maingrid[i+piece_y][j+piece_x+1] = 0
    piece_x, piece_y = x, y
    poser(piece, x,y)

# Testé et fonctionnel 
def randombloc():
    global activebloc
    activebloc = bloc = choice([cyan, blue, orange, yellow, green, purple, red])
    return bloc
# Utiliser poser(randombloc(), x, y) pour générer un bloc aléatoire

