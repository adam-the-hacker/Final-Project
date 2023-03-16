import pieces, tetris


def rotation(piece):
    piece2 = [[0 for i in range(len(piece[0]))] for j in range(len(piece))]
    for x in range(len(piece)):
        for y in range(len(piece)):
            piece2[y][len(piece)-1-x] = piece[x][y]
    return piece2


def mouvement(piece, direction):
    npiece =                            



'''       À CONTINUER APRES LA FONCTION DU MOUVEMENT DES PIÈCES

def iscolision(piece, direction): # -1 pour la gauche 
    for y in piece:
        for x in y:
            if piece[y][x] > 0 and maingrid[y][x+direction] == 1:
                return True                                         # Renvoie vrai s'il y a une colision
            elif piece[x][y] == 0:
                continue
'''                     
