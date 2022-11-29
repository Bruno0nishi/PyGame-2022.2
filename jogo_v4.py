import pygame
from pygame.locals import *
from Sprites import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864
screen_height = 936

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flapper Birb')


#variaveis do jogo
mexe_chao = 0
vel_scroll = 4
flying = False
game_over = False
cano_gap = 150
cano_frequencia = 1500  #milisegundos
last_cano = pygame.time.get_ticks() - cano_frequencia


bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')



bird_group = pygame.sprite.Group()
cano_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)


run = True
while run:

    clock.tick(fps)

    #Fundo
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()
    cano_group.draw(screen)

    screen.blit(ground_img, (mexe_chao, 768))

    #Colisão com o cano
    if pygame.sprite.groupcollide(bird_group, cano_group, False, False) or flappy.rect.top < 0:
        game_over = True

    #Colisão com o chão
    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False


    if game_over == False and flying == True:

        #Gera canos
        time_now = pygame.time.get_ticks()
        if time_now - last_cano > cano_frequencia:
            cano_height = random.randint(-100, 100)
            btm_cano = Cano(screen_width, int(screen_height / 2) + cano_height, -1)
            top_cano = Cano(screen_width, int(screen_height / 2) + cano_height, 1)
            cano_group.add(btm_cano)
            cano_group.add(top_cano)
            last_cano = time_now


        #Chão se mexendo
        mexe_chao -= vel_scroll
        if abs(mexe_chao) > 35:
            mexe_chao = 0

        cano_group.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()