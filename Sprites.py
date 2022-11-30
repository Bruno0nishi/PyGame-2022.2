import pygame
from pygame.locals import *
import random

flying = False
game_over = False

CHAO_ALTURA = 100

#variaveis do jogo
mexe_chao = 0
vel_scroll = 4
flying = False
game_over = False


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

            #Animação
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
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/Pipe.png')
        self.rect = self.image.get_rect()
        
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(cano_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(cano_gap / 2)]

    def update(self):
        self.rect.x -= vel_scroll
        if self.rect.right < 0:
            self.kill()


class Botao():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        action = False

        posicao = pygame.mouse.get_pos()

        if self.rect.collidepoint(posicao):
            if pygame.mouse.get_pressed()[0] == 1:
                action = True

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action
