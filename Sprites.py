import pygame
from pygame.locals import *
import random

flying = False
game_over = False

CHAO_ALTURA = 100

CANO_WIDTH  = 90
CANO_HEIGHT = 600
cano_gap_inicio = 180
cano_gap = cano_gap_inicio
cano_minimo = 30
screen_width = 864
screen_height= 936
vel_jogo= -4

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.clicked = False

    def update(self):

        if flying == True:
            #Gravidade
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over == False:
            #Pulo
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            #animação
            self.counter += 1
            bate_asa = 5

            if self.counter > bate_asa:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            
            self.image = pygame.transform.rotate(self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)
 
          
class Cano(pygame.sprite.Sprite):
    def __init__(self, invertido, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.cordocano = {pygame.transform.scale(pygame.image.load('img/pipe.png'), (CANO_WIDTH, CANO_HEIGHT))}

        self.rect.center = [x, y]
        self.invertido = invertido
        self.image = self.cordocano
        self.rect = self.image.get_rect()
        self.rect.left = screen_height-20
        self.posicaox = 0

        if self.invertido:
            self.image = pygame.transform.flip(self.image,False,True)
            self.rect.x  = - canonormal.rect.left
            self.rect.y = - canonormal.rect.top + cano_gap

        else:
            self.posicaox = random.randint(cano_minimo+cano_gap, -CHAO_ALTURA-cano_minimo)
            self.rect.top = self.posicaox


    def update(self):

        if self.invertido:
            self.image = pygame.transform.flip(self.image,False,True)
        self.movimentovertical()

    def movimentovertical(self):
        if self.invertido:
            self.rect.left = canonormal.rect.left
            self.rect.bottom = canonormal.rect.top - cano_gap
        else:
            self.rect.x += vel_jogo
            if self.rect.right <= 0:
                self.rect.left = screen_width
                self.posicaox =  random.randint(cano_minimo+cano_gap, -CHAO_ALTURA-cano_minimo)
            self.rect.top = self.posicaox

    def jogardenovo(self):
        if self.invertido:
            self.rect.left = canonormal.rect.left
            self.rect.bottom = canonormal.rect.top - cano_gap
        else:
            self.rect.left = -20
            self.posicaox = random.randint(cano_minimo+cano_gap, -CHAO_ALTURA-cano_minimo)
            self.rect.top = self.posicaox
            
all_sprites = pygame.sprite.Group()
canos   = pygame.sprite.Group()
canonormal = Cano(False)
canoinvert = Cano(True)
canos.add(canonormal)
canos.add(canoinvert)

all_sprites.add(canonormal)