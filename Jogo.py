# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:31:07 2020

"""

import pygame


pygame.init()

RED = (255, 0, 0, 255)
YELLOW = (255, 255, 0, 255)
WHITE = (255, 255, 255, 255)
BLACK = (0, 0, 0, 255)

WIDTH = 800
HEIGHT = 800
WIDTH_CAIXA_TEXTO = 770
HEIGHT_CAIXA_TEXTO = 200
TEXT_SIZE = 18
WIDTH_BUTTON = 250
HEIGHT_BUTTON = 70

font_name = pygame.font.match_font('arial')

TEXTO_WIDTH_1 = WIDTH/4 - 155
TEXTO_HEIGHT_1 = HEIGHT - 185
TEXTO_WIDTH_2 = WIDTH/4 - 155
TEXTO_HEIGHT_2 = (HEIGHT - 20) - 185

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DEAD BUT NOT SO DEAD')


def draw_text(window, text, size, width, height):
    font = pygame.font.Font(font_name, size)
    text_window = font.render(text, True, (WHITE))
    text_rect = text_window.get_rect()
    text_rect.midtop = (width, height)
    window.blit(text_window, text_rect)

def load_recursos():
    recursos = {}
    recursos['posto_gasolina_1'] = pygame.image.load('imgs/posto_gasolina_1.png').convert()
    recursos['caixa_texto'] = pygame.image.load('imgs/caixa_texto.png').convert()
    recursos['caixa_texto'] = pygame.transform.scale(recursos['caixa_texto'], (WIDTH_CAIXA_TEXTO, HEIGHT_CAIXA_TEXTO))
    recursos['button'] = pygame.image.load('imgs/button.png').convert()
    recursos['button'] = pygame.transform.scale(recursos['button'], (WIDTH_BUTTON, HEIGHT_BUTTON)) 
    
    return recursos
class Caixa_de_texto(pygame.sprite.Sprite):
    def __init__(self, recursos):
        
        pygame.sprite.Sprite.__init__(self)

        self.image = recursos['caixa_texto']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.recursos = recursos

class Button_1(pygame.sprite.Sprite): # a base esta = 590 / o topo esta = 660 / a esquerda esta = 16 / a direita esta = 266
    def __init__(self, recursos):

        pygame.sprite.Sprite.__init__(self)

        self.image = recursos['button']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = 16
        self.rect.bottom = HEIGHT - 210
        self.recursos = recursos

class Button_2(pygame.sprite.Sprite): # a base esta = 590 / o topo esta = 660 / a esquerda esta = 276 / a direita esta = 526
    def __init__(self, recursos):

        pygame.sprite.Sprite.__init__(self)

        self.image = recursos['button']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = 276
        self.rect.bottom = HEIGHT - 210
        self.recursos = recursos

class Button_3(pygame.sprite.Sprite): # a base esta = 590 / o topo esta = 660 / a esquerda esta = 536 / a direita esta = 786
    def __init__(self, recursos):

        pygame.sprite.Sprite.__init__(self)

        self.image = recursos['button']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left = 536
        self.rect.bottom = HEIGHT - 210
        self.recursos = recursos

def tela_jogo(window):
    recursos = load_recursos()
    
    all_sprites = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    
    caixa_texto = Caixa_de_texto(recursos)
    button_1 = Button_1(recursos)
    button_2 = Button_2(recursos)
    button_3 = Button_3(recursos)
    all_sprites.add(caixa_texto)
    all_sprites.add(button_1)
    all_sprites.add(button_2)
    all_sprites.add(button_3)
    
    contagem_img = 1 # Serve para mudar as imgs de fundo
    contagem_txt = 1 # Serve para mudar os textos
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                px = event.pos[0]
                py = event.pos[1]
                if contagem_txt == 1:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 2
                        
                elif contagem_txt == 2:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 3
                        
                elif contagem_txt == 3:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                        game = False
                        
        if contagem_txt == 1:
            text_1 = 'teste 1'
            text_2 = 'teste 2'
        if contagem_txt == 2:
            text_1 = 'Hello'
            text_2 = 'World'
        if contagem_txt == 3:
            text_1 = ''
            text_2 = ''
        
        all_sprites.update()
        
        window.fill(BLACK)
        window.blit(recursos['posto_gasolina_1'], (0, 0))
        all_sprites.draw(window)

        draw_text(window, text_1, TEXT_SIZE, TEXTO_WIDTH_1, TEXTO_HEIGHT_1)
        draw_text(window, text_2, TEXT_SIZE, TEXTO_WIDTH_2, TEXTO_HEIGHT_2)
        

        pygame.display.update()
        
tela_jogo(window)
    
pygame.quit()
