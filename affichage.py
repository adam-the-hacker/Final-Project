
# Testé et fonctionnel
def showgrid():
  for y in range(len(maingrid)):
    for x in range(len(maingrid[1])):
        if maingrid[y][x] == 0:
            fenetre.blit(blocblanc, ((x-1)*30,y*30)) # Le coef 30 existe car ce sont les dimensions d'un carré
        if maingrid[y][x] == 1 or maingrid[y][x] == 11:
            fenetre.blit(bloccyan, ((x-1)*30,y*30))
        if maingrid[y][x] == 2 or maingrid[y][x] == 22:
            fenetre.blit(blocblue, ((x-1)*30,y*30))
        if maingrid[y][x] == 3 or maingrid[y][x] == 33:
            fenetre.blit(blocorange, ((x-1)*30,y*30))
        if maingrid[y][x] == 4 or maingrid[y][x] == 44:
            fenetre.blit(blocyellow, ((x-1)*30,y*30))
        if maingrid[y][x] == 5 or maingrid[y][x] == 55:
            fenetre.blit(blocgreen, ((x-1)*30,y*30))
        if maingrid[y][x] == 6 or maingrid[y][x] == 66:
            fenetre.blit(blocpurple, ((x-1)*30,y*30))
        if maingrid[y][x] == 7 or maingrid[y][x] == 77:
            fenetre.blit(blocred, ((x-1)*30,y*30))
        if maingrid[y][x] == 8:
            fenetre.blit(blocscore, ((x-1)*30,y*30))


def hardsetbloc(piece):
    global piece_x, piece_y

    # Récupérer le nombre de la pièce
    npiece = 0
    for z in range(len(piece)):
        for v in range(len(piece[0])):
            if piece[z][v] != 0:
                npiece = piece[z][v]

    # Doubler ce nombre
    nblocdur = int(str(npiece) + str(npiece))

    # Effacer
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

    # Générer la matrice du bloc dur
    piecedur = piece
    for x in range(len(piecedur)):
        for y in range(len(piecedur[0])):
            if piecedur[x][y] == npiece:
                piecedur[x][y] = nblocdur

    # Poser en dur

    poser(piecedur, piece_x, piece_y)
