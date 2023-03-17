# Main code
from pygame import*
from math import*
import time
from random import*
from functions import *
from pieces import *

maingrid = [[9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9],
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9], 
            [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9]]

init()

blocblanc = image.load('Bloc blanc.PNG')
bloccyan = image.load('Bloc cyan.PNG')
blocblue = image.load('Bloc blue.PNG')
blocorange = image.load('Bloc orange.PNG')
blocyellow = image.load('Bloc yellow.PNG')
blocgreen = image.load('Bloc green.PNG')
blocpurple = image.load('Bloc purple.PNG')
blocred = image.load('Bloc red.PNG')

fenetre = display.set_mode((300,600), RESIZABLE)  # Obligation sur la taille : 2x = y
                                                  # Si vous voulez changer la taille de l'interface,
                                                  # changez la taille de tous les carrés telle que pour
                                                  # chaque carré, x(interface) = 10*x(carré)
                                                  # et un coef de 20 pour les y

while True:
    showgrid()
    display.flip()
