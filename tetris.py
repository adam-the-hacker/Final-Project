# Main code
import random
import time as t
from pygame import*
from math import*
from random import*
from pieces import*

""" VARIABLES """

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
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]

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
lbloc = [bloccyan, blocblue, blocorange, blocyellow, blocgreen, blocpurple, blocred]

fenetre = display.set_mode((480,600), RESIZABLE)

isactivepiece = 0 # Si cette variable est égale à 1, alors on appelle la fonction poser(bloc) pour générer un bloc aléatoire
                        # Si elle est égale à 0, on attend que le bloc soit posé pour la mettre à 1 et donc générer un nouveau bloc
piece_x = 0
piece_y = 0
comp = 0
continuer = 1
vspeed = 10         # Vertical speed, On le réduira pour augmenter la difficulté
level = vspeed // 10
temps = t.time()
rotated_bloc = 0
piece0 = True
activebloc = None
score = 0
high_scores=open("score.txt", "a+")
totallines = 0
nextblocs = []
# Génération du premier bloc
nextblocs.append(choice([cyan, blue, orange, yellow, green, purple, red]))

""" MAIN CODE """

while continuer == 1:
    time.Clock().tick(10)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0

    if isactivepiece == 0:
        # Premier bloc
        activebloc = nextblocs[0]
        # Supprimer ce bloc de la liste
        nextblocs.pop(0)
        # Générer un nouveau bloc aléatoire et l'ajouter à la liste des prochains blocs à afficher à droite du jeu
        nextblocs.append(choice([cyan, blue, orange, yellow, green, purple, red]))
        piece_y = 0
        piece_x = 3
        if collision(activebloc):
            break # stoppe le jeu et affche le score ect...
        isactivepiece = 1

    keyb = key.get_pressed()

    if keyb[K_RIGHT]:
        piece_x += 1
        if collision(activebloc):
            piece_x -= 1

    if keyb[K_LEFT]:
        piece_x -= 1
        if collision(activebloc):
            piece_x +=1

    if keyb[K_SPACE]:
        while not collision(activebloc):
            piece_y += 1
        piece_y -=1
        score+=10 #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!??

    if keyb[K_DOWN]:
        piece_y += 1
        if collision(activebloc):
            piece_y -= 1
        score += 1

    if keyb[K_UP]:
        activebloc2 = activebloc
        activebloc2 = rotate_piece(activebloc2)
        if collision(activebloc2):
            continue
        else:
            activebloc = rotate_piece(activebloc)

    if comp % (vspeed) == 0:
        piece_y += 1
        if collision(activebloc):
            piece_y -= 1
            poser(activebloc, piece_x, piece_y)
            isactivepiece = 0

    # Affichage
    showgrid()

    affichepiece(activebloc)
    destroyline()
    display.flip()
    comp += 1

# On met le score dans un doc
high_scores.write(str(score)+"\n")
high_scores.close()
# Syntaxes :
# Lire le fichier: open("score.txt","r")
# Le lire ligne par ligne: high_scores_list = high_scores.readlines.
