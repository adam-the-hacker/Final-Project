import random
import time as t
from pygame import*
from math import*
from random import*



""""""""""""""""""""""""""" PIECES """""""""""""""""""""""""""

cyan = [[0, 0, 0, 0],
        [1, 1, 1, 1],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]

blue = [[2, 0, 0],
        [2, 2, 2],
        [0, 0, 0]]

orange = [[0, 0, 3],
          [3, 3, 3],
          [0, 0, 0]]

yellow = [[4, 4],
          [4, 4]]

green = [[0, 5, 5],
         [5, 5, 0],
         [0, 0, 0]]

purple = [[0, 6, 0],
          [6, 6, 6],
          [0, 0, 0]]

red = [[7, 7, 0],
       [0, 7, 7],
       [0, 0, 0]]



""""""""""""""""""""""""""" VARIABLES """""""""""""""""""""""""""

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

### VARIABLES VISUELLES

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
homescreen = image.load('Homescreen.png')
screenmenu = image.load('Screenmenu.png')
screenmusic = image.load('Screenmusic.png')
startscreen0 = image.load('0.png')
startscreen1 = image.load('1.png')
startscreen2 = image.load('2.png')
startscreen3 = image.load('3.png')
pausescreen = image.load('Pausescreen.png')
fenetre = display.set_mode((480,600), RESIZABLE)

music = True # Music is on by default
font = font.SysFont("consolas", 30, bold=True, italic=False)


### RELATIF À LA PARTIE

continuer = 2
continued = False
isactivepiece = 0
# Si cette variable est égale à 1, alors on appelle la fonction poser(bloc) pour générer un bloc aléatoire
# Si elle est égale à 0, on attend que le bloc soit posé pour la mettre à 1 et donc générer un nouveau bloc


### RELATIF AUX PIÈCES

piece_x = 0
piece_y = 0
shadow_piece_y = piece_y

nextbloc = choice([cyan, blue, orange, yellow, green, purple, red])
lbloc = [bloccyan, blocblue, blocorange, blocyellow, blocgreen, blocpurple, blocred]
activebloc = None
piece0 = True
rotated_bloc = 0
drop = False


### RELATIF AU FONCTIONNEMENT

comp = 0
vspeed = 10 # Vertical speed, On le réduira pour augmenter la difficulté
level = vspeed // 10 # Changer la formule du level
clavier_actif = 100
temps = t.time()


### RELATIF AU SCORE

score = 0
high_scores = open("score.txt", "a+")
file = open("score.txt", "r")
totallines = 0
stringlastscores = []

for x in file:
    if x != "\n" and x != 0 and x != "0\n":
        stringlastscores.append(x)

for x in range(len(stringlastscores)):
    stringlastscores[x] = stringlastscores[x].replace("\n", "")

lastscores = sorted(stringlastscores, key=int, reverse=False)
try:
    lastscore1 = font.render(lastscores[-1], True, (255, 255, 255))
    lastscore2 = font.render(lastscores[-2], True, (255, 255, 255))
    lastscore3 = font.render(lastscores[-3], True, (255, 255, 255))
    lastscore4 = font.render(lastscores[-4], True, (255, 255, 255))
    lastscore5 = font.render(lastscores[-5], True, (255, 255, 255))
except:
    pass



""""""""""""""""""""""""""" FONCTIONS """""""""""""""""""""""""""

def rotate_piece(piece):
    piece2 = [[0 for x in range(len(piece))] for y in range(len(piece[0]))]
    for x in range(len(piece[0])):
        for y in range(len(piece)):
            piece2[x][y] = piece[len(piece) - y - 1][x]
    piece = piece2
    return piece

def poser(piece, x, y):
    global piece_x, piece_y
    piece_x, piece_y = x, y
    for i in range(len(piece)):
        for j in range(len(piece[0])):
            if piece[i][j] != 0:
                maingrid[i+y][j+x+1] = piece[i][j]

def collision(piece):
    global maingrid, piece_x, piece_y
    for y in range(len(piece)):
        for x in range(len(piece)):
            if piece[y][x] != 0:
                if maingrid[piece_y + y][piece_x + x + 1] != 0:
                    return True
    return False

def collision_shadow(piece):
    global maingrid, piece_x, shadow_piece_y
    for y in range(len(piece)):
        for x in range(len(piece)):
            if piece[y][x] != 0:
                if maingrid[shadow_piece_y + y][piece_x + x + 1] != 0:
                    return True
    return False

def destroyline():
    global score, level, completedlines, totallines
    completedlines = 0
    destroyed = False

    for y in range(len(maingrid) - 3):
        if all(maingrid[y]):
            maingrid.pop(y)
            maingrid.insert(0, [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 8, 8, 8, 8, 8])
            completedlines += 1
            totallines += 1
            destroyed = True

    if destroyed:
        score += ((100 + 200 * (completedlines - 1)) * level)

def showgrid():
  for y in range(len(maingrid)):
    for x in range(len(maingrid[1])):
        if maingrid[y][x] == 0:
            fenetre.blit(blocblanc, ((x-1)*30,y*30)) # Le coef 30 existe car ce sont les dimensions d'un carré
        if maingrid[y][x] == 1:
            fenetre.blit(bloccyan, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 2:
            fenetre.blit(blocblue, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 3:
            fenetre.blit(blocorange, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 4:
            fenetre.blit(blocyellow, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 5:
            fenetre.blit(blocgreen, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 6:
            fenetre.blit(blocpurple, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 7:
            fenetre.blit(blocred, ((x - 1) * 30, y * 30))
        if maingrid[y][x] == 8:
            fenetre.blit(blocscore, ((x-1)*30,y*30))

def affichepiece(piece):
    global piece_x, piece_y
    for l in range(len(piece)):
        for c in range(len(piece)):
            if piece[l][c] != 0:
                fenetre.blit(lbloc[piece[l][c] - 1], ((piece_x + c) * 30, (piece_y + l) * 30))

def affichepiece2(piece, x, y):
    for l in range(len(piece)):
        for c in range(len(piece)):
            if piece[l][c] != 0:
                fenetre.blit(lbloc[piece[l][c] - 1], ((x + c) * 30, (y + l) * 30))



""""""""""""""""""""""""""" STARTING SCREENS """""""""""""""""""""""""""


while continuer == 2:
    time.Clock().tick(15)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0
    keyb = key.get_pressed()
    if keyb[K_e]:
        continuer = 1
    if keyb[K_o]:
        menu = True
        musiccomp = 0
        while menu:
            time.Clock().tick(10)
            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0
                    menu = False
            keyb = key.get_pressed()

            if keyb[K_m]:
                musiccomp += 1
                if musiccomp % 2 == 0:
                    music = True
                else:
                    music = False

            if keyb[K_RETURN]:
                menu = False

            if not music:
                fenetre.blit(screenmusic, (0, 0))
            else:
                fenetre.blit(screenmenu, (0, 0))

            display.flip()

    fenetre.blit(homescreen, (0, 0))
    try:
        fenetre.blit(lastscore1, (240-10*len(lastscores[-1]), 370))
        fenetre.blit(lastscore2, (240-10*len(lastscores[-2]), 400))
        fenetre.blit(lastscore3, (240-10*len(lastscores[-3]), 430))
        fenetre.blit(lastscore4, (240-10*len(lastscores[-4]), 460))
        fenetre.blit(lastscore5, (240-10*len(lastscores[-5]), 490))
    except:
        pass
    display.flip()

if music:
    # Load music
    mixer.music.load('Korobeiniki.mp3')
    # Loop music
    mixer.music.play(-1)

fenetre.blit(startscreen3, (0, 0))
fenetre.blit(scoreboard, (300, 0))
display.flip()
time.wait(1000)

fenetre.blit(startscreen2, (0, 0))
fenetre.blit(scoreboard, (300, 0))
display.flip()
time.wait(1000)

fenetre.blit(startscreen1, (0, 0))
fenetre.blit(scoreboard, (300, 0))
display.flip()
time.wait(1000)

fenetre.blit(startscreen0, (0, 0))
fenetre.blit(scoreboard, (300, 0))
display.flip()


""""""""""""""""""""""""""" MAIN CODE """""""""""""""""""""""""""


while continuer == 1:
    clavier_actif += 1
    time.Clock().tick(100)

    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0

    if continued:
        showgrid()
        fenetre.blit(scoreboard, (300, 0))
        affichepiece(activebloc)
        destroyline()
        fenetre.blit(font.render(str(score), True, (0, 0, 0)), (350, 103))
        fenetre.blit(font.render(str(totallines), True, (0, 0, 0)), (375, 338))
        affichepiece2(nextbloc, 11.3, 15)
        display.flip()
        continued = False

    ### GÉNÉRER LES PIECES

    if isactivepiece == 0:
        time.wait(500)
        # Premier bloc
        activebloc = nextbloc
        # Supprimer ce bloc de la liste
        nextbloc = choice([cyan, blue, orange, yellow, green, purple, red])
        # Générer un nouveau bloc aléatoire et l'ajouter à la liste des prochains blocs à afficher à droite du jeu
        piece_y = 0
        piece_x = 3
        if collision(activebloc):
            break  # stoppe le jeu et affche le score ect...
        isactivepiece = 1

    keyb = key.get_pressed()

    ### PAUSE MENU

    if keyb[K_p] and clavier_actif > 20:

        pause = True
        while pause:
            time.Clock().tick(10)
            for evenements in event.get():
                if evenements.type == QUIT:
                    continuer = 0
                    pause = False
            keyb = key.get_pressed()

            if keyb[K_p] and clavier_actif > 20:
                clavier_actif = 0
                pause = False

            if keyb[K_o]:
                menu = True
                musiccomp = 0
                while menu:
                    time.Clock().tick(10)
                    for evenements in event.get():
                        if evenements.type == QUIT:
                            continuer = 0
                            menu = False
                    keyb = key.get_pressed()

                    if keyb[K_m]:
                        if music == False and musiccomp == 0:
                            music = True
                            mixer.music.load('Korobeiniki.mp3')
                            mixer.music.play(-1)
                            continue
                        musiccomp += 1
                        if musiccomp % 2 == 0:
                            music = True
                            mixer.music.unpause()
                        else:
                            music = False
                            mixer.music.pause()

                    if keyb[K_RETURN]:
                        menu = False

                    if not music:
                        fenetre.blit(screenmusic, (0, 0))
                    else:
                        fenetre.blit(screenmenu, (0, 0))

                    display.flip()


            fenetre.blit(pausescreen, (0, 0))
            try:
                fenetre.blit(lastscore1, (240 - 10 * len(lastscores[-1]), 370))
                fenetre.blit(lastscore2, (240 - 10 * len(lastscores[-2]), 400))
                fenetre.blit(lastscore3, (240 - 10 * len(lastscores[-3]), 430))
                fenetre.blit(lastscore4, (240 - 10 * len(lastscores[-4]), 460))
                fenetre.blit(lastscore5, (240 - 10 * len(lastscores[-5]), 490))
            except:
                pass
            display.flip()



    ### COMMANDES CLAVIER

    if keyb[K_RIGHT] and clavier_actif > 5:
        clavier_actif = 0
        piece_x += 1
        if collision(activebloc):
            piece_x -= 1

    if keyb[K_LEFT] and clavier_actif > 5:
        clavier_actif = 0
        piece_x -= 1
        if collision(activebloc):
            piece_x +=1

    ### HARD DROP

    if keyb[K_SPACE]:
            if not drop:
                drop = True
                while not collision(activebloc):
                    piece_y += 1
                    score += 2
                piece_y -= 1
                score -= 1
                poser(activebloc, piece_x, piece_y)
                isactivepiece = 0
                continued = True
                continue
    else:
        drop = False

    if keyb[K_DOWN] and clavier_actif > 3:
        clavier_actif = 0
        piece_y += 1
        score += 1
        if collision(activebloc):
            piece_y -= 1
            score -= 1
            poser(activebloc, piece_x, piece_y)
            isactivepiece = 0
            continued = True
            continue

    ### TOURNER

    if keyb[K_UP] and clavier_actif > 7:
        clavier_actif = 0
        activebloc2 = activebloc
        activebloc2 = rotate_piece(activebloc2)
        if collision(activebloc2):
            pass
        else:
            activebloc = rotate_piece(activebloc)

    if comp % 65 == 0:
        piece_y += 1
        if collision(activebloc):
            piece_y -= 1
            poser(activebloc, piece_x, piece_y)
            isactivepiece = 0
            continued = True
            continue


    ### AFFICHAGE

    showgrid()
    fenetre.blit(scoreboard, (300, 0))
    affichepiece(activebloc)
    destroyline()

    # Affichage du score, lignes, ect

    fenetre.blit(font.render(str(score), True, (0, 0, 0)), (350, 103))
    fenetre.blit(font.render(str(totallines), True, (0, 0, 0)), (375, 338))
    affichepiece2(nextbloc, 11.5 - (len(nextbloc) - 3) / 2, 15)

    # Affichage de l'ombre de la pièce

    shadow_piece = list(activebloc)
    shadow_piece_y = piece_y
    if collision_shadow(shadow_piece):
        shadow_piece_y -= 1
    while not collision_shadow(shadow_piece):
        shadow_piece_y += 1
    shadow_piece_y -= 1
    affichepiece2(shadow_piece, piece_x, shadow_piece_y)
    display.flip()
    comp += 1

### SCORE

high_scores.write(str(score)+"\n")
high_scores.close()
# Syntaxes :
# Lire le fichier: open("score.txt","r")
