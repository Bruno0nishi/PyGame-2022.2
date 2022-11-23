import random
from tkinter.tix import Tree
import pygame
import time

pygame.init()

# ----- Gera tela principal
WIDTH = 360
HEIGHT = 640
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Flappy Bird')

# ----- Inicia estruturas de dados
game = True

# ----- Inicia assets
image = pygame.image.load('Assets/img/background.png').convert()
image = pygame.transform.scale(image, (360,640))

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