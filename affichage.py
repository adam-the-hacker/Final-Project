import Tetris

def showgrid():
  for y in range(len(maingrid)):
    for x in range(len(maingrid[1])):
      if maingrid[y][x] == 0:
      '''
      Si 0, afficher case noire
      Si 1, afficher le bloc de la couleur correspondante
      Si 2, même chose... ect
      Si 9, afficher vide
      '''
