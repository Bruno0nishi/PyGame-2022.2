import random
from tkinter.tix import Tree
import pygame
import time
from Sprites import bird 
pygame.init()

# ----- Gera tela principal
WIDTH = 370
HEIGHT = 640
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')


# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('Assets/img/background.png').convert_alpha()
image = pygame.transform.scale(image, (WIDTH, HEIGHT))

bird_img = pygame.image.load("assets/img/bird.png").convert_alpha()
bird_img = pygame.transform.scale(bird_img, (200, 200))
fox = bird(bird_img, 150, 295)
i = 0

# Define nome da janela e icone
pygame.display.set_caption("Jumpy Fox")
icone = pygame.image.load("./Assets/img/bird.png")
pygame.display.set_icon(icone)

# Define loop principal, posicao inicial, pontos iniciais e carrega fonte
game = True
jogo = True
pontos = 0
posicaox = 0
fonte = pygame.font.SysFont("comicsans", 30, True)


# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (10, 10))


    # ----- Atualiza estado do jogo
    
    pygame.display.update()

pygame.quit()