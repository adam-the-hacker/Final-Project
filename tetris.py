# Main code
from pygame import*
from math import*
import time
from random import*
import pieces, functions

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

''' L'interface est en 537 par 1067, mais je peux changer ''' 
fenetre = display.set_mode((537, 1067), RESIZABLE) 