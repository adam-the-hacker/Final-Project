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
scoreboard = image.load('scoreboard.png')
lbloc = [bloccyan, blocblue, blocorange, blocyellow, blocgreen, blocpurple, blocred]

fenetre = display.set_mode((480,600), RESIZABLE)

isactivepiece = 0 # Si cette variable est égale à 1, alors on appelle la fonction poser(bloc) pour générer un bloc aléatoire
                        # Si elle est égale à 0, on attend que le bloc soit posé pour la mettre à 1 et donc générer un nouveau bloc
font = font.SysFont ("consolas", 30, bold=True, italic=False)
piece_x = 0
piece_y = 0
comp = 0
continuer = 1
vspeed = 10         # Vertical speed, On le réduira pour augmenter la difficulté

# il faut changer la formule du level
level = vspeed // 10

temps = t.time()
rotated_bloc = 0
piece0 = True
activebloc = None
score = 0
high_scores=open("score.txt", "a+")
totallines = 0
nextbloc = choice([cyan, blue, orange, yellow, green, purple, red])

""" MAIN CODE """

while continuer == 1:
    time.Clock().tick(10)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0

        if isactivepiece == 0:
        # Premier bloc
        activebloc = nextbloc
        # Supprimer ce bloc de la liste
        nextbloc = choice([cyan, blue, orange, yellow, green, purple, red])
        # Générer un nouveau bloc aléatoire et l'ajouter à la liste des prochains blocs à afficher à droite du jeu
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
            score+=2
        piece_y -= 1
        score -= 1

    if keyb[K_DOWN]:
        piece_y += 1
        score += 1
        if collision(activebloc):
            piece_y -= 1
            score -= 1

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
            # Scoreboard
    fenetre.blit(scoreboard, (300, 0))
    affichepiece(activebloc)
    destroyline()
            # Score
    fenetre.blit(font.render(str(score), True, (0, 0, 0)), (350, 103))
    fenetre.blit(font.render(str(totallines), True, (0, 0, 0)), (375, 338))
    affichepiece2(nextbloc, 11.5-(len(nextbloc)-3)/2, 15)
    display.flip()
    comp += 1

# On met le score dans un doc
high_scores.write(str(score)+"\n")
high_scores.close()
# Syntaxes :
# Lire le fichier: open("score.txt","r")
# Le lire ligne par ligne: high_scores_list = high_scores.readlines.
