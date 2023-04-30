while continuer == 1:
    time.Clock().tick(10)
    for evenements in event.get():
        if evenements.type == QUIT:
            continuer = 0

    if isactivepiece == 0:
        activebloc = choice([cyan, blue, orange, yellow, green, purple, red])
        piece_y = 0
        piece_x = 3
        if collision(activebloc):
            continue # stoppe le jeu et affche le score ect...
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

#On met le score dans un doc
high_scores.write(str(score)+"\n")
high_scores.close()
# Syntaxes :
# Lire le fichier: open("score.txt","r")
# Le lire ligne par ligne: high_scores_list = high_scores.readlines.
