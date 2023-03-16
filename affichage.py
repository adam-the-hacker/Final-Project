import Tetris

def showgrid():
  for y in range(len(maingrid)):
    for x in range(len(maingrid[1])):
      if maingrid[y][x] == 0:
