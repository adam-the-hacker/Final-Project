import Tetris


# Testé et fonctionnel
def showgrid():
  for y in range(len(maingrid)):
    for x in range(len(maingrid[1])):
        if maingrid[y][x] == 0:
            fenetre.blit(blocblanc, ((x-1)*30,y*30)) # Le coef 30 existe car ce sont les dimensions d'un carré
        if maingrid[y][x] == 1:
            fenetre.blit(bloccyan, ((x-1)*30,y*30))
        if maingrid[y][x] == 2:
            fenetre.blit(blocblue, ((x-1)*30,y*30))
        if maingrid[y][x] == 3:
            fenetre.blit(blocorange, ((x-1)*30,y*30))
        if maingrid[y][x] == 4:
            fenetre.blit(blocyellow, ((x-1)*30,y*30))
        if maingrid[y][x] == 5:
            fenetre.blit(blocgreen, ((x-1)*30,y*30))
        if maingrid[y][x] == 6:
            fenetre.blit(blocpurple, ((x-1)*30,y*30))
        if maingrid[y][x] == 7:
            fenetre.blit(blocred, ((x-1)*30,y*30))
        if maingrid[y][x] == 8:
            fenetre.blit(blocscore, ((x-1)*30,y*30))
