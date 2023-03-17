from pieces import *
from tetris import maingrid

# Testé et fonctionnel
def rotation(piece):
    piece2 = [[0 for i in range(len(piece[0]))] for j in range(len(piece))]
    for x in range(len(piece)):
        for y in range(len(piece)):
            piece2[y][len(piece)-1-x] = piece[x][y]
    return piece2

# A compléter puis tester
def mouvement(piece, direction):             # -1 pour gauche et 1 pour droite
    for i in range(len(piece)):
        for j in range(len(piece[1])):
            if piece[i][j] > 0:
                npiece = piece[i][j]
    for y in range(len(maingrid)):
        for x in range(len(maingrid[1])):
            if maingrid[y][x] == npiece:
                if iscolision(piece, direction):
                    break
                else:
                    maingrid[y][x] = maingrid[y][x+direction]
                    maingrid[y][x] = 0


''' Pas fini
# Colisions avec 8 et 9

def iscolision(piece, direction): # -1 pour la gauche et 1 pour la droite
    for y in maingrid:
        for x in y:
            if maingrid[y][x+direction] == 9 or if maingrid[y][x+direction] == 8:
                return True
    return False
'''
                    
                    
# Testé et fonctionnel
def poser(piece):
    for i in range(len(piece)):
        for j in range(len(piece[1])):
            maingrid[i][j + 5] = piece[i][j]
            
bloc = random.choice([cyan, blue, orange, yellow, green, purple, red])
# Utiliser poser(bloc) pour générer un bloc aléatoire


