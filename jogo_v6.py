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


font = pygame.font.SysFont('Bauhaus 93', 60)

cor_fonte = (255, 255, 255)

# variaveis do jogo
mexe_chao = 0
vel_jogo = 4
flying = False
game_over = False
cano_gap = 150
cano_frequencia = 1500  # milisegundos
last_cano = pygame.time.get_ticks() - cano_frequencia
pontuação = 0
passou_cano = False


bg = pygame.image.load('img/bg.png')
ground_img = pygame.image.load('img/ground.png')


def fonte_pontuacao(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class Bird(pygame.sprite.Sprite):
    def _init_(self, x, y):
        pygame.sprite.Sprite._init_(self)
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
            # Gravidade
            self.vel += 0.5
            if self.vel > 8:
                self.vel = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.vel)

        if game_over == False:
            # Pulo
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.vel = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            # Animação
            self.counter += 1
            bate_asa = 5

            if self.counter > bate_asa:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]

            self.image = pygame.transform.rotate(
                self.images[self.index], self.vel * -2)
        else:
            self.image = pygame.transform.rotate(self.images[self.index], -90)


class cano(pygame.sprite.Sprite):
    def _init_(self, x, y, position):
        pygame.sprite.Sprite._init_(self)
        self.image = pygame.image.load('img/Pipe.png')
        self.rect = self.image.get_rect()

        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(cano_gap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(cano_gap / 2)]

    def update(self):
        self.rect.x -= vel_jogo
        if self.rect.right < 0:
            self.kill()


bird_group = pygame.sprite.Group()
cano_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2))

bird_group.add(flappy)


run = True
while run:

    clock.tick(fps)

    # Fundo
    screen.blit(bg, (0, 0))

    bird_group.draw(screen)
    bird_group.update()
    cano_group.draw(screen)

    screen.blit(ground_img, (mexe_chao, 768))

    # Pontuação
    if len(cano_group) > 0:
        if bird_group.sprites()[0].rect.left > cano_group.sprites()[0].rect.left\
                and bird_group.sprites()[0].rect.right < cano_group.sprites()[0].rect.right\
                and passou_cano == False:
            passou_cano = True
        if passou_cano == True:
            if bird_group.sprites()[0].rect.left > cano_group.sprites()[0].rect.right:
                pontuação += 1
                passou_cano = False

    fonte_pontuacao(str(pontuação), font, cor_fonte, int(screen_width / 2), 20)

    # Colisão com o cano
    if pygame.sprite.groupcollide(bird_group, cano_group, False, False) or flappy.rect.top < 0:
        game_over = True

    # colisão com o chão
    if flappy.rect.bottom >= 768:
        game_over = True
        flying = False

    if game_over == False and flying == True:

        # Gera Canos
        time_now = pygame.time.get_ticks()
        if time_now - last_cano > cano_frequencia:
            cano_height = random.randint(-100, 100)
            btm_cano = cano(screen_width, int(
                screen_height / 2) + cano_height, -1)
            top_cano = cano(screen_width, int(
                screen_height / 2) + cano_height, 1)
            cano_group.add(btm_cano)
            cano_group.add(top_cano)
            last_cano = time_now

        # Chão se mexendo
        mexe_chao -= vel_jogo
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