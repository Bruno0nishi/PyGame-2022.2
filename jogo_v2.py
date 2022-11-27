import random 
import sys
import pygame
from pygame.locals import * 


#GLOBAL VARIABLES 

FPS = 32
SCREENWIDTH = 289
SCREENHEIGHT = 511
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
GROUNDY = SCREENHEIGHT*0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = 'resources\SPRITES\\bird.png'
BACKGROUND = 'resources\SPRITES\\bg.jpeg'
PIPE = 'resources\SPRITES\pipe.png '