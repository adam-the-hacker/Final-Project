import time as t
from pygame import *
from random import *

# Initialisation
continuer = 1
init()
mixer.init()

# Police par défaut sur le jeu
font = font.SysFont("consolas", 30, bold=True, italic=False)

# Boucle principale qui permet de jouer plusieurs fois sans relancer le programme python
while True and continuer != 0:
    time.Clock().tick(10)
    init()
    """"""""""""""""""""""""""" PIECES """""""""""""""""""""""""""
    # chaque pièce comporte son propre numéro

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

    # 9 : case fantôme, qui ne s'affiche pas
    # 0 : case vierge (s'affiche noire)
    # 8 : case fantôme, qui permet juste de laisser de l'espace pour le score et délimiter la zone de jeu

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
    gameover1 = image.load('Gameover1.png')
    gameover2 = image.load('Gameover2.png')
    namescreen = image.load('yourscore.png')

    # ombre des pièces
    shadowcyan = image.load('shadowcyan.PNG')
    shadowblue = image.load('shadowblue.PNG')
    shadoworange = image.load('shadoworange.PNG')
    shadowyellow = image.load('shadowyellow.PNG')
    shadowgreen = image.load('shadowgreen.PNG')
    shadowpurple = image.load('shadowpurple.PNG')
    shadowred = image.load('shadowred.PNG')

    # Fenêtre de 480 par 600
    fenetre = display.set_mode((480, 600), RESIZABLE)

    music = True  # La musique est allumée par défaut

    ### RELATIF À LA PARTIE

    # continuer = 1 : jeu principal
    # continuer = 2 : start menu
    # continuer = 3 : game over
    # continuer = 4 : demander le nom du joueur
    continuer = 2

    # Se met à True si on utilise la ligne "continue" du programme
    continued = False

    # Se met à 1 si une pièce est active dans le jeu
    isactivepiece = 0

    ### RELATIF AUX PIÈCES

    # Coordonnées de la pièce active
    piece_x = 0
    piece_y = 0
    shadow_piece_y = piece_y

    # Choix du prochain bloc
    nextbloc = choice([cyan, blue, orange, yellow, green, purple, red])

    # Liste de blocs
    lbloc = [bloccyan, blocblue, blocorange, blocyellow, blocgreen, blocpurple, blocred]
    lblocshadow = [shadowcyan, shadowblue, shadoworange, shadowyellow, shadowgreen, shadowpurple, shadowred]

    # Stocke le bloc actif dans une variable
    activebloc = None

    # Se met à True si on appuie sur le hard drop afin de bloquer la touche temporairement
    drop = False

    ### RELATIF AU FONCTIONNEMENT

    # utilisé plus tard pour faire clignoter le "game over" à la fin de la partie
    k = 0

    # utilisé comme compteur afin de compter les tours de boucle ect
    comp = 0

    # Vertical speed, on le réduira pour augmenter la difficulté.
    # Ce nombre est le nombre de tours de boucle nécessaire afin de descendre la pièce active
    vspeed = 65

    # niveau actuel
    level = 1

    # pour controler le clavier
    clavier_actif = 100

    # utilisé afin de controller un bruitage a la fin du jeu. J'ai eu peu d'originalité
    randomvariable = 0

    ### RELATIF AU SCORE

    # score
    score = 0

    # ouvrir le fichier afin de le lire et de le modifier
    high_scores = open("score.txt", "a+")

    # ouvrir le fichier afin de le lire seulement
    file = open("score.txt", "r")

    # lignes détruites
    totallines = 0

    # liste des scores précédents sous forme de chaine de caractères
    stringlastscores = []

    # liste des noms enregistrés
    nameslist = []

    ### Nom du joueur

    # zone de texte
    input_box = Rect(173, 325, 123, 42)  # CHANGER LA POSITION

    # nom du joueur (s'update en direct à chaque fois que le joueur écris une lettre de son nom)
    username = ''

    # variable qui est utile lors de la gestion de la zone de texte
    active = True

    # séparer le fichier en une liste de noms et de scores
    for x in file:
        line = x.split(" ")
        if x != "\n" and x != 0 and x != "0\n":
            line[0] = line[0].replace("\n", "")
            stringlastscores.append(line[0])
            try:
                line[1] = line[1].replace("\n", "")
                nameslist.append(line[1])
            except:
                nameslist.append("")

    # remplacer tous les caractères indésirables par un caractère vide
    for x in range(len(stringlastscores)):
        stringlastscores[x] = stringlastscores[x].replace("\n", "")

    # Trie les scores et associe les noms correspondants
    sorted_scores_with_names = sorted(zip(stringlastscores, nameslist), key=lambda x: int(x[0]), reverse=False)

    # Sépare les scores triés et les noms dans deux listes distinctes
    try:
        lastscores, nameslist = zip(*sorted_scores_with_names)
    except:
        pass

    # enregistre les scores précédents (s'ils existent) sous forme de variables
    try:
        lastscore1 = font.render(str(lastscores[-1] + " " + nameslist[-1]), True, (255, 255, 255))
        lastscore2 = font.render(str(lastscores[-2] + " " + nameslist[-2]), True, (255, 255, 255))
        lastscore3 = font.render(str(lastscores[-3] + " " + nameslist[-3]), True, (255, 255, 255))
        lastscore4 = font.render(str(lastscores[-4] + " " + nameslist[-4]), True, (255, 255, 255))
        lastscore5 = font.render(str(lastscores[-5] + " " + nameslist[-5]), True, (255, 255, 255))
    except:
        pass

    """"""""""""""""""""""""""" FONCTIONS """""""""""""""""""""""""""


    def rotate_piece(piece):
        piece2 = [[0 for x in range(len(piece))] for y in range(len(piece[0]))]
        mixer.Sound.play(mixer.Sound('Rotate.wav'))
        for x in range(len(piece[0])):
            for y in range(len(piece)):
                piece2[x][y] = piece[len(piece) - y - 1][x]
        piece = piece2
        return piece


    def poser(piece, x, y):
        global piece_x, piece_y
        piece_x, piece_y = x, y
        mixer.Sound.play(mixer.Sound('Landing.wav'))
        for i in range(len(piece)):
            for j in range(len(piece[0])):
                if piece[i][j] != 0:
                    maingrid[i + y][j + x + 1] = piece[i][j]


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
            mixer.Sound.play(mixer.Sound('Yay.wav'))


    def showgrid():
        for y in range(len(maingrid)):
            for x in range(len(maingrid[1])):
                if maingrid[y][x] == 0:
                    fenetre.blit(blocblanc,
                                 ((x - 1) * 30, y * 30))  # Le coef 30 existe car ce sont les dimensions d'un carré
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
                    fenetre.blit(blocscore, ((x - 1) * 30, y * 30))


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


    def affichepiece3(piece, x, y):
        for l in range(len(piece)):
            for c in range(len(piece)):
                if piece[l][c] != 0:
                    fenetre.blit(lblocshadow[piece[l][c] - 1], ((x + c) * 30, (y + l) * 30))


    """"""""""""""""""""""""""" STARTING SCREENS """""""""""""""""""""""""""

    if music:
        mixer.music.load('HomeScreen.mp3')
        mixer.music.play(-1)

    while continuer == 2:
        time.Clock().tick(15)
        for evenements in event.get():
            if evenements.type == QUIT:
                continuer = 0
                break
        keyb = key.get_pressed()
        if keyb[K_e]:
            continuer = 1
        if keyb[K_o]:
            menu = True
            # compte le nombre de fois que la touche m est appuyée
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
                    # permet de switcher entre l'arrêt et l'activation de la musique
                    if musiccomp % 2 == 0:
                        music = True
                        mixer.music.unpause()

                    else:
                        music = False
                        mixer.music.pause()

                if keyb[K_f]:
                    with open("score.txt", "r") as fichier:
                        data = fichier.readlines()
                    with open("score.txt", "w") as fichier:
                        for line in data:
                            fichier.write('')
                    lastscores = []
                    menu = False

                if keyb[K_RETURN]:
                    menu = False

                if not music:
                    fenetre.blit(screenmusic, (0, 0))
                else:
                    fenetre.blit(screenmenu, (0, 0))

                display.flip()

        fenetre.blit(homescreen, (0, 0))
        try:
            fenetre.blit(lastscore1, (240 - 10 * len(lastscores[-1]) - 10 * len(nameslist[-1]), 370))
            fenetre.blit(lastscore2, (240 - 10 * len(lastscores[-2]) - 10 * len(nameslist[-2]), 400))
            fenetre.blit(lastscore3, (240 - 10 * len(lastscores[-3]) - 10 * len(nameslist[-3]), 430))
            fenetre.blit(lastscore4, (240 - 10 * len(lastscores[-4]) - 10 * len(nameslist[-4]), 460))
            fenetre.blit(lastscore5, (240 - 10 * len(lastscores[-5]) - 10 * len(nameslist[-5]), 490))
        except:
            pass
        display.flip()

    if music:
        # Stop homescreen music
        mixer.music.stop()
        # Load music
        mixer.music.load('Korobeiniki.mp3')
        # Loop music
        mixer.music.play(-1)

    mixer.Sound.play(mixer.Sound('GameStart.wav'))

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

        time.Clock().tick(100)

        for evenements in event.get():
            if evenements.type == QUIT:
                continuer = 0
                break

        if continued:
            showgrid()
            fenetre.blit(scoreboard, (300, 0))
            affichepiece(activebloc)
            destroyline()
            fenetre.blit(font.render(str(score), True, (0, 0, 0)), (350, 103))
            fenetre.blit(font.render(str(level), True, (0, 0, 0)), (375, 239))
            fenetre.blit(font.render(str(totallines), True, (0, 0, 0)), (375, 338))
            affichepiece2(nextbloc, 11.5 - (len(nextbloc) - 3) / 2, 15)
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
                continuer = 4
            isactivepiece = 1

        keyb = key.get_pressed()

        ### PAUSE MENU

        if keyb[K_p] and clavier_actif > 20:

            pause = True
            mixer.Sound.play(mixer.Sound('Pause.wav'))
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
                    mixer.Sound.play(mixer.Sound('Pause.wav'))

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
                                mixer.music.unpause()
                                continue
                            musiccomp += 1
                            if musiccomp % 2 == 0:
                                music = True
                                mixer.music.unpause()
                            else:
                                music = False
                                mixer.music.pause()

                        if keyb[K_f]:
                            with open("score.txt", "r") as fichier:
                                data = fichier.readlines()
                            with open("score.txt", "w") as fichier:
                                for line in data:
                                    fichier.write('')
                            lastscores = []
                            menu = False

                        if keyb[K_RETURN]:
                            menu = False
                            mixer.Sound.play(mixer.Sound('Select.wav'))

                        if not music:
                            fenetre.blit(screenmusic, (0, 0))
                            mixer.music.pause()
                        else:
                            fenetre.blit(screenmenu, (0, 0))

                        display.flip()

                fenetre.blit(pausescreen, (0, 0))
                try:
                    fenetre.blit(lastscore1, (240 - 10 * len(lastscores[-1]) - 10 * len(nameslist[-1]), 370))
                    fenetre.blit(lastscore2, (240 - 10 * len(lastscores[-2]) - 10 * len(nameslist[-2]), 400))
                    fenetre.blit(lastscore3, (240 - 10 * len(lastscores[-3]) - 10 * len(nameslist[-3]), 430))
                    fenetre.blit(lastscore4, (240 - 10 * len(lastscores[-4]) - 10 * len(nameslist[-4]), 460))
                    fenetre.blit(lastscore5, (240 - 10 * len(lastscores[-5]) - 10 * len(nameslist[-5]), 490))
                except:
                    pass
                display.flip()

        ### COMMANDES CLAVIER

        if keyb[K_RIGHT] and clavier_actif > 5:
            clavier_actif = 0
            piece_x += 1
            mixer.Sound.play(mixer.Sound('Move.wav'))
            if collision(activebloc):
                piece_x -= 1

        if keyb[K_LEFT] and clavier_actif > 5:
            clavier_actif = 0
            piece_x -= 1
            mixer.Sound.play(mixer.Sound('Move.wav'))
            if collision(activebloc):
                piece_x += 1

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
                mixer.Sound.play(mixer.Sound('HardDrop.wav'))
                isactivepiece = 0
                continued = True
                continue
        else:
            drop = False

        if keyb[K_DOWN] and clavier_actif > 3:
            clavier_actif = 0
            piece_y += 1
            score += 1
            mixer.Sound.play(mixer.Sound('Move.wav'))
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

        if comp % vspeed == 0:
            piece_y += 1
            if collision(activebloc):
                piece_y -= 1
                poser(activebloc, piece_x, piece_y)
                isactivepiece = 0
                continued = True
                continue

        if score > 5000 * level and vspeed > 3:
            vspeed -= 3
            level += 1

        ### AFFICHAGE

        showgrid()
        fenetre.blit(scoreboard, (300, 0))
        destroyline()

        # Affichage du score, lignes, ect

        fenetre.blit(font.render(str(score), True, (0, 0, 0)), (350, 103))
        fenetre.blit(font.render(str(level), True, (0, 0, 0)), (375, 239))
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
        affichepiece3(shadow_piece, piece_x, shadow_piece_y)
        affichepiece(activebloc)
        display.flip()
        comp += 1
        clavier_actif += 1

    ### SCORE
    if score != 0:
        high_scores.write(str(score) + " ")
    # Syntaxes :
    # Lire le fichier: open("score.txt","r")

    """"""""""""""""""""""""""" PLAYER NAME """""""""""""""""""""""""""

    while continuer == 4:

        time.Clock().tick(15)

        for evenements in event.get():
            if evenements.type == QUIT:
                continuer = 0
                break
            if evenements.type == KEYDOWN:
                if active:
                    if evenements.key == K_RETURN:
                        high_scores.write(str(username) + "\n")
                        username = ''
                        continuer = 3
                    elif evenements.key == K_BACKSPACE:
                        username = username[:-1]
                    else:
                        if len(username) < 6:
                            username += evenements.unicode

        fenetre.blit(namescreen, (0, 0))
        fenetre.blit(font.render(str(score), True, (255, 255, 255)), (240 - 10 * len(str(score)), 250))
        color = Color('white')  # CHANGER LA COULEUR DU TEXTE
        txt_surface = font.render(username, True, color)
        fenetre.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        draw.rect(fenetre, Color('black'), input_box, 2)

        display.flip()

    """"""""""""""""""""""""""" GAME OVER """""""""""""""""""""""""""
    time.wait(300)
    while continuer == 3:

        time.Clock().tick(15)

        if randomvariable == 0:
            mixer.Sound.play(mixer.Sound('KO.wav'))
            randomvariable = 1

        for evenements in event.get():
            if evenements.type == QUIT:
                continuer = 0
                break

        keyb = key.get_pressed()

        if keyb[K_RETURN]:
            continuer = 2

        if k % 2 == 0:
            fenetre.blit(gameover1, (0, 0))
        else:
            fenetre.blit(gameover2, (0, 0))

        high_scores = open("score.txt", "a+")
        file = open("score.txt", "r")
        totallines = 0
        stringlastscores = []

        nameslist = []

        for x in file:
            line = x.split(" ")
            if x != "\n" and x != 0 and x != "0\n":
                line[0] = line[0].replace("\n", "")
                stringlastscores.append(line[0])
                try:
                    line[1] = line[1].replace("\n", "")
                    nameslist.append(line[1])
                except:
                    nameslist.append("")

        for x in range(len(stringlastscores)):
            stringlastscores[x] = stringlastscores[x].replace("\n", "")

        # Trie les scores et associe les noms correspondants
        sorted_scores_with_names = sorted(zip(stringlastscores, nameslist), key=lambda x: int(x[0]), reverse=False)

        # Sépare les scores triés et les noms dans deux listes distinctes
        lastscores, nameslist = zip(*sorted_scores_with_names)

        try:
            lastscore1 = font.render(str(lastscores[-1] + " " + nameslist[-1]), True, (255, 255, 255))
            lastscore2 = font.render(str(lastscores[-2] + " " + nameslist[-2]), True, (255, 255, 255))
            lastscore3 = font.render(str(lastscores[-3] + " " + nameslist[-3]), True, (255, 255, 255))
            lastscore4 = font.render(str(lastscores[-4] + " " + nameslist[-4]), True, (255, 255, 255))
            lastscore5 = font.render(str(lastscores[-5] + " " + nameslist[-5]), True, (255, 255, 255))
        except:
            pass

        try:
            fenetre.blit(lastscore1, (240 - 10 * len(lastscores[-1]) - 10 * len(nameslist[-1]), 370))
            fenetre.blit(lastscore2, (240 - 10 * len(lastscores[-2]) - 10 * len(nameslist[-2]), 400))
            fenetre.blit(lastscore3, (240 - 10 * len(lastscores[-3]) - 10 * len(nameslist[-3]), 430))
            fenetre.blit(lastscore4, (240 - 10 * len(lastscores[-4]) - 10 * len(nameslist[-4]), 460))
            fenetre.blit(lastscore5, (240 - 10 * len(lastscores[-5]) - 10 * len(nameslist[-5]), 490))
        except:
            pass

        display.flip()
        time.wait(200)
        k += 1
