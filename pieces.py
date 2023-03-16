### LISTE DES PIÈCES
# https://static.wikia.nocookie.net/tetrisconcept/images/c/ca/Tetromino_image.png/revision/latest?cb=20090706171943
import random

cyan=[[1,1,1,1],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]]

blue=[[2,0,0],
     [2,2,2],
     [0,0,0]]

orange=[[0,0,3],
        [3,3,3],
        [0,0,0]]

yellow=[[4,4],
        [4,4]]

green=[[0,5,5],
       [5,5,0],
       [0,0,0]]

purple=[[0,6,0],
        [6,6,6],
        [0,0,0]]

red=[[7,7,0],
     [0,7,7],
     [0,0,0]]

bloc = random.choice([cyan, blue, orange, yellow, green, purple, red])
