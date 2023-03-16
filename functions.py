import pieces, tetris

def rotation(piece):
    piece2 = [[0 for i in range(len(piece[0]))] for j in range(len(piece))]
    for x in range(len(piece)):
        for y in range(len(piece)):
            piece2[y][len(piece)-1-x] = piece[x][y]
    return piece2

def colision(piece):
    if main
