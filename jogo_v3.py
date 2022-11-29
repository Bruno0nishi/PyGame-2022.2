
import pygame
from pygame.locals import *
from Sprites import *
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


bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')


bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)


run = True
while run:

    clock.tick(fps)

    #Fundo
    screen.blit(bg, (0,0))

    bird_group.draw(screen)
    bird_group.update()


    screen.blit(ground_img, (mexe_chao, 768))

    #Contato com o chão
    if flappy.rect.bottom > 768:
        game_over = True
        flying = False


    if game_over == False:
        #Fundo se mexendo
        mexe_chao -= vel_scroll
        if abs(mexe_chao) > 35:
            mexe_chao = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and flying == False and game_over == False:
            flying = True

    pygame.display.update()

pygame.quit()