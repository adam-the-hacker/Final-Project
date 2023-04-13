from pieces import *
from tetris import maingrid

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
            if piece[i][j] != 0:
                maingrid[i+y][j+x+1] = piece[i][j]
                
def affichepiece(piece):
    global piece_x, piece_y
    for l in range(len(piece)):
        for c in range(len(piece)):
            if piece[l][c] != 0:
                fenetre.blit(lbloc[piece[l][c] - 1], ((piece_x + c) * 30, (piece_y + l) * 30))


def collision(piece):
    global maingrid, piece_x, piece_y
    for y in range(len(piece)):
        for x in range(len(piece)):
            if piece[y][x] != 0:
                if maingrid[piece_y + y][piece_x + x + 1] != 0:
                    return True
    return False


def destroyline():
    global iscompleted, completedlines, score, level
    completedlines = []

    # Recherche de lignes complètes
    for y in range(len(maingrid)-3):
        iscompleted = all(maingrid[y]) # Fonction très utile trouvée sur internet,
                                        # elle permet de return True si une liste ne contient pas de 0
        if iscompleted:
            completedlines.append(y)

    # Destruction des lignes complètes
    for y in completedlines:
        for x in range(len(maingrid[0])):
            if maingrid[y][x] not in [8, 9]:
                maingrid[y][x] = 0
                score += ((100 + 200*(len(completedlines)-1))*level)//10

    print(len(completedlines))

    move_blocks_down(len(completedlines))


# J'ai utilisé un peu d'aide pour déplacer la ligne détruite vers le bas
def move_blocks_down(num_lines):
    if num_lines == 0:
        return None

    for y in range(len(maingrid)-1, num_lines-1, -1):
        for x in range(len(maingrid[y])):
            if maingrid[y][x] not in [0, 8, 9]:
                # Déplace ce bloc vers le bas de num_lines lignes
                for i in range(num_lines):
                    if y+i+1 >= len(maingrid) or maingrid[y+i+1][x] in [8,9]:
                        break
                else:
                    maingrid[y+num_lines][x] = maingrid[y][x]
                    maingrid[y][x] = 0
