# Main code
from pygame import*
from math import*
import time
from random import*
from functions import *
from pieces import *

maingrid = [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8]]

init()
blocblanc = image.load('Bloc blanc.PNG')
bloccyan = image.load('Bloc cyan.PNG')
blocblue = image.load('Bloc blue.PNG')
blocorange = image.load('Bloc orange.PNG')
blocyellow = image.load('Bloc yellow.PNG')
blocgreen = image.load('Bloc green.PNG')
blocpurple = image.load('Bloc purple.PNG')
blocred = image.load('Bloc red.PNG')
blocscore = image.load('Bloc score.PNG')
fenetre = display.set_mode((480,600), RESIZABLE)


isactivepiece = 0 # Si cette variable est égale à 1, alors on appelle la fonction poser(bloc) pour générer un bloc aléatoire
                        # Si elle est égale à 0, on attend que le bloc soit posé pour la mettre à 1 et donc générer un nouveau bloc
piece_x = 0
piece_y = 0
comp = 0
continuer = 1
vspeed = 9         # Vertical speed, On le réduira pour augmenter la difficulté
temps = t.time()
rotated_bloc = 0
piece0 = True



while continuer == 1:
    time.Clock().tick(9)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    if isactivepiece == 0:
        if piece0:
            rotated_bloc = 0
            poser(randombloc(), 3, -1)
            isactivepiece = 1
        else:
            rotated_bloc = 0
            poser(randombloc(), 3, 0)
            isactivepiece = 1

    keyb = key.get_pressed()
    if keyb[K_RIGHT] and piece_x + 1 < 11 - len(activebloc[0]):
        deplacer_piece(activebloc, piece_x + 1, piece_y)

    if keyb[K_LEFT] and piece_x > 0:
        deplacer_piece(activebloc, piece_x - 1, piece_y)

    if keyb[K_SPACE]:
        continue

    if keyb[K_DOWN] and piece_y < 19:
        deplacer_piece(activebloc, piece_x, piece_y + 1)

    if keyb[K_UP]:
        rotated_bloc += 1
        deplacer_piece(activebloc, piece_x, piece_y)

    if comp % (vspeed) == 0 and piece_y < 18:
        deplacer_piece(activebloc, piece_x, piece_y + 1)
        #print(t.time()-temps)

    if piece_y == 18:
        hardsetbloc(activebloc)
        isactivepiece = 0
        piece0 = False


    showgrid()
    display.flip()
    comp += 1

