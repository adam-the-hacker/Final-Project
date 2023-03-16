import pieces, tetris


def rotation(piece):
    piece2 = [[0 for i in range(len(piece[0]))] for j in range(len(piece))]
    for x in range(len(piece)):
        for y in range(len(piece)):
            piece2[y][len(piece)-1-x] = piece[x][y]
    return piece2


def mouvement(piece, direction):             # -1 pour gauche et 1 pour droite
    npiece = piece[1][1]
    for y in maingrid:
        for x in y:
            if maingrid[y][x] == npiece:
                if iscolision(piece, direction):
                    break
                else:
                    maingrid[y][x] = maingrid[y][x+direction]

                    
def iscolision(piece, direction): # -1 pour la gauche et 1 pour la droite
    npiece = piece[1][1]
    for y in maingrid:
        for x in y:
            if maingrid[y][x+direction] == 9:
                return True
    return False
