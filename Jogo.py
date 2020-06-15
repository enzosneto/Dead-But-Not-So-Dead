# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:31:07 2020
"""

import pygame
from teste_game_screen import game_screen

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

DIALOGO_WIDTH_1_1 = WIDTH/4 - 170
DIALOGO_HEIGHT_1_1 = HEIGHT - 260

DIALOGO_WIDTH_1_2 = WIDTH/4 - 170
DIALOGO_HEIGHT_1_2 = HEIGHT - 240

# - - - - - -  - - - - - - - - - -  - - - -

DIALOGO_WIDTH_2_1 = WIDTH/4 + 90
DIALOGO_HEIGHT_2_1 = HEIGHT - 260

DIALOGO_WIDTH_2_2 = WIDTH/4 + 90
DIALOGO_HEIGHT_2_2 = HEIGHT - 240

# - - - - - -  - - - - - - - - - -  - - - -

DIALOGO_WIDTH_3_1 = WIDTH/4 + 350
DIALOGO_HEIGHT_3_1 = HEIGHT - 260

DIALOGO_WIDTH_3_2 = WIDTH/4 + 350
DIALOGO_HEIGHT_3_2 = HEIGHT - 240

# - - - - - -  - - - - - - - - - -  - - - -

TEXTO_WIDTH_1 = WIDTH/4 - 175
TEXTO_HEIGHT_1 = (HEIGHT - 20) - 175

TEXTO_WIDTH_2 = WIDTH/4 - 175
TEXTO_HEIGHT_2 = HEIGHT - 175

TEXTO_WIDTH_3 = WIDTH/4 - 175
TEXTO_HEIGHT_3 = (HEIGHT + 20) - 175

TEXTO_WIDTH_4 = WIDTH/4 - 175
TEXTO_HEIGHT_4 = (HEIGHT + 40) - 175

TEXTO_WIDTH_5 = WIDTH/4 - 175
TEXTO_HEIGHT_5 = (HEIGHT + 60) - 175

TEXTO_WIDTH_6 = WIDTH/4 - 175
TEXTO_HEIGHT_6 = (HEIGHT + 80) - 175

TEXTO_WIDTH_7 = WIDTH/4 - 175
TEXTO_HEIGHT_7 = (HEIGHT + 100) - 175

TEXTO_WIDTH_8 = WIDTH/4 - 175
TEXTO_HEIGHT_8 = (HEIGHT + 120) - 175

TEXTO_WIDTH_9 = WIDTH/4 - 175
TEXTO_HEIGHT_9 = (HEIGHT + 140) - 175

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('DEAD BUT NOT SO DEAD')


def draw_text(window, text, size, width, height):
    font = pygame.font.Font(font_name, size)
    text_window = font.render(text, True, (WHITE))
    text_rect = text_window.get_rect()
    text_rect.midleft = (width, height)
    window.blit(text_window, text_rect)

def load_recursos():
    recursos = {}
    recursos['caixa_texto'] = pygame.image.load('imgs/caixa_texto.png').convert()
    recursos['caixa_texto'] = pygame.transform.scale(recursos['caixa_texto'], (WIDTH_CAIXA_TEXTO, HEIGHT_CAIXA_TEXTO))
    recursos['button'] = pygame.image.load('imgs/button.png').convert()
    recursos['button'] = pygame.transform.scale(recursos['button'], (WIDTH_BUTTON, HEIGHT_BUTTON)) 
    
    #colocar as imagens aqui, copiar o do posto de gasolina linha 2248
    recursos['1'] = pygame.image.load('imgs/1.png').convert()
    recursos['2'] = pygame.image.load('imgs/2.png').convert()
    recursos['3'] = pygame.image.load('imgs/3.png').convert()
    recursos['4'] = pygame.image.load('imgs/4.png').convert()
    recursos['5'] = pygame.image.load('imgs/5.png').convert()
    recursos['6'] = pygame.image.load('imgs/6.png').convert()
    recursos['7'] = pygame.image.load('imgs/7.png').convert()
    recursos['8'] = pygame.image.load('imgs/8.png').convert()
    recursos['9'] = pygame.image.load('imgs/9.png').convert()
    recursos['10'] = pygame.image.load('imgs/10.png').convert()
    recursos['11'] = pygame.image.load('imgs/11.png').convert()
    recursos['12'] = pygame.image.load('imgs/12.png').convert()
    recursos['13'] = pygame.image.load('imgs/13.png').convert()
    recursos['14'] = pygame.image.load('imgs/14.png').convert()
    recursos['15'] = pygame.image.load('imgs/15.png').convert()
    recursos['16'] = pygame.image.load('imgs/16.png').convert()
    recursos['17'] = pygame.image.load('imgs/17.png').convert()
    recursos['18'] = pygame.image.load('imgs/18.png').convert()
    recursos['19'] = pygame.image.load('imgs/19.png').convert()
    recursos['20'] = pygame.image.load('imgs/20.png').convert()
    recursos['21'] = pygame.image.load('imgs/21.png').convert()
    recursos['22'] = pygame.image.load('imgs/22.png').convert()
    recursos['23'] = pygame.image.load('imgs/23.png').convert()
    recursos['24'] = pygame.image.load('imgs/24.png').convert()
    recursos['25'] = pygame.image.load('imgs/25.png').convert()
    recursos['26'] = pygame.image.load('imgs/26.png').convert()
    recursos['27'] = pygame.image.load('imgs/27.png').convert()
    recursos['28'] = pygame.image.load('imgs/28.png').convert()
    recursos['29'] = pygame.image.load('imgs/29.png').convert()
    recursos['30'] = pygame.image.load('imgs/30.png').convert()
    recursos['31'] = pygame.image.load('imgs/31.png').convert()
    recursos['32'] = pygame.image.load('imgs/32.png').convert()
    recursos['33'] = pygame.image.load('imgs/33.png').convert()
    recursos['34'] = pygame.image.load('imgs/34.png').convert()
    recursos['35'] = pygame.image.load('imgs/35.png').convert()
    recursos['36'] = pygame.image.load('imgs/36.png').convert()
    
    
    #esse da capa eh um teste
    recursos['teste'] = pygame.image.load('imgs/capa.png').convert()
    
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
    
    contagem_txt = 0 # Serve para mudar os textos
    contagem_filha = 0 #Serve para acabar o jogo caso a filha fique brava
    
    MORTO = False
    # morto = game_screen(window, MORTO)
    
    game = True
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                px = event.pos[0]
                py = event.pos[1]
                #print(px)
                #print(py)
                if contagem_txt == 0:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                        if px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                            contagem_txt = 1
                    
                        elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                            game = False      
                        
                elif contagem_txt == 1:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 2
                        
                elif contagem_txt == 2:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 3
                        
                elif contagem_txt == 3:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 4
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 4
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 4               
                        
                #Aumenta o contador do texto para mudar o que aparece escrito
                elif contagem_txt == 4:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 5
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 5
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_filha += 1
                        contagem_txt = 5 
                         
                elif contagem_txt == 5:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 6
                        
                elif contagem_txt == 6:   
                    if px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 8
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 7 
                         
                elif contagem_txt == 7:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 7.5
                         
                elif contagem_txt == 7.5:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 8
                         
                elif contagem_txt == 8:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 9
                         
                elif contagem_txt == 9:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 10
                         
                elif contagem_txt == 10:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 10.5
                
                elif contagem_txt == 10.5:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 11
                
                elif contagem_txt == 11:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 12
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 12
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 12 
                         
                elif contagem_txt == 12:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 13
                        
                elif contagem_txt == 13:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 14
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 14
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 14
                         
                elif contagem_txt == 14:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 15
                         # game_screen(window, morto)  # Inicia o mini game 
                         game_screen(window, MORTO)
                         # morto = game_screen(window, morto)
                         #if morto == False:
                          #   contagem_txt = 15
                         #else:
                          #   game = False
                         
                elif contagem_txt == 15:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 16
                         
                elif contagem_txt == 16:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 17
                         
                elif contagem_txt == 17:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 18
                         
                elif contagem_txt == 18:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 19
                         
                elif contagem_txt == 19:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 21
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 21
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_filha += 1
                        contagem_txt = 20

                elif contagem_txt == 20:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 21
                         
                elif contagem_txt == 21:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 22
                         
                elif contagem_txt == 22:
                    if px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 23
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 26
                         
                elif contagem_txt == 23:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 24
                         
                elif contagem_txt == 24:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 25
                         
                elif contagem_txt == 25:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 26
                        
                elif contagem_txt == 26:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 27
                         
                elif contagem_txt == 27:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 28
                         
                elif contagem_txt == 28:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 29
                         
                elif contagem_txt == 29:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 30
                         
                elif contagem_txt == 30:
                    if px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 31
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 32
                
                elif contagem_txt == 31:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 33
                         
                elif contagem_txt == 32:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 33
                         
                elif contagem_txt == 33:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 34
                         
                elif contagem_txt == 34:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 35
                         
                elif contagem_txt == 35:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 37
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 37
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_filha += 1
                        contagem_txt = 36
                         
                elif contagem_txt == 36:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 37
                         
                elif contagem_txt == 37:
                    if px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 38
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 39
                         
                elif contagem_txt == 38:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 39
                         
                elif contagem_txt == 39:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 40
                        
                elif contagem_txt == 40:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 41
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 41
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 41
                         
                elif contagem_txt == 41:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 42
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 43
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 43
                         
                elif contagem_txt == 42:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 43
                         
                elif contagem_txt == 43:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 45
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 45
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_filha += 1
                        contagem_txt = 44
                         
                elif contagem_txt == 44:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 45
                         
                elif contagem_txt == 45:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 46
                         
                elif contagem_txt == 46:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 47
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 47
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 47
                        
                elif contagem_txt == 47:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 48
                         
                elif contagem_txt == 48:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 50
                         
                elif contagem_txt == 50:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 51
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 51
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 51
                         
                elif contagem_txt == 51:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 52
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 52
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 52
                         
                elif contagem_txt == 52:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 53
                         
                elif contagem_txt == 53:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 54
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 54
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 54
                         
                elif contagem_txt == 54:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 55
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 55
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 55
                        
                elif contagem_txt == 55:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 56
                         
                elif contagem_txt == 56:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 57
                         
                elif contagem_txt == 57:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_filha += 1
                        contagem_txt = 58
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 59
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 59
                        
                elif contagem_txt == 58:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 59
                        
                elif contagem_txt == 59:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 60
                         
                elif contagem_txt == 60:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_filha += 1
                        contagem_txt = 61
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 62
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 62
                        
                elif contagem_txt == 61:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 62
                        
                elif contagem_txt == 62:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 63
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 63
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 63
                        
                elif contagem_txt == 63:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 64
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 64
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 64
                        
                elif contagem_txt == 64:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 65
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 65
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 65
                        
                elif contagem_txt == 65:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 66
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 66
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 69
                        
                elif contagem_txt == 66:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 67
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 67
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 67
                        
                elif contagem_txt == 67:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 68
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 68
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 68
                        
                        #vai pro final
                elif contagem_txt == 68:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                        contagem_txt = 72
                    
                elif contagem_txt == 69:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 70
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 70
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 70
                        
                elif contagem_txt == 70:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 71
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 71
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 71
                #vai pro final
                elif contagem_txt == 71:
                    if px > 16 and px < 266 and py > 520 and py < 590: # Botão 1
                        
                        contagem_txt = 72
                    
                    elif px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                        contagem_txt = 72
                    
                    elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                        contagem_txt = 72
                        
                elif contagem_txt == 72:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 73
                         
                elif contagem_txt == 73:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                        if px > 277 and px < 523 and py > 520 and py < 590: # Botão 2
                        
                            contagem_txt = 1
                    
                        elif px > 537 and px < 784 and py > 520 and py < 590: # Botão 3
                        
                            game = False
                         
            
        #Todas as falas e textos do jogo
                       
        if contagem_txt == 0:
            dialogo_1_1 = 'Escolha um dos dois:'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Start game'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Quit game'
            dialogo_3_2 = ''
            
            text_1 = 'Bem vindo ao nosso jogo. Voce agora vai entrar nos pés de um pai de família tentando manter sua filhia viva no fim'
            text_2 = 'do mundo. O que voce vai experênciar é uma simulação de como seria o fim do mundo (provavelmente).'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = 'Criado por:'
            text_7 = 'Pedro Ball'
            text_8 = 'Enzo Cardoso'
            text_9 = 'Luis Fernando'
         
        elif contagem_txt == 1:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Em um início de noite de sexta feira, você e sua filha estão voltando pra casa depois de buscar ela na escola.'
            text_2 = 'Vocês tiveram que fazer uma parada rápida num posto de gasolina para abastecer seu carro.'
            text_3 = 'Enquanto abastecia o carro, você percebe que o rádio que estava tocando musicas lofi hip hop por 24 horas seguidas'
            text_4 = 'é interrompido, e começa a transmitir o que parece ser uma transmissão emergencial de uma estação de notícia'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 2:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Atenção cidadãos americanos, isso é de extrema importância. Como sabem, nossa grande nação foi recentemente'
            text_2 = 'atingida com um vírus novo, a Covid-19. Como resposta, o governo distribuiu pílulas providas da cloroquina.'
            text_3 = 'Porém, após algumas semanas, percebemos que o vírus sofreu uma mutação como resposta á pílula.'
            text_4 = 'O novo vírus, chamado de Covid-20, infecta não só os pulmões como o córtex cerebral também,o que causa '
            text_5 = 'com que o infectado aja de maneira agressiva. Por essa razão pedimos que fiquem em casa e tranquem suas portas.'
            text_6 = 'As forças armadas já estão sendo enviadas para controlar a situação. Evitem centros urbanos se puderem.'
            text_7 = 'Permaneçam em suas casas e fiquem atentos á futuros avisos. Que Deus ajude e abençoe o povo americano.'
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 3:
            dialogo_1_1 = 'Claro, vai ficar tudo bem'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Essa midia é muito fantasiosa,'
            dialogo_2_2 = 'tao inventando coisa'
            
            dialogo_3_1 = 'Eu sinceramente não sei docinho'
            dialogo_3_2 = ''
            
            text_1 = '"Nossa pai, ainda abem que o senhor não é pró Trump e não fomos tomar a cloroquina, mas o rádio falou '
            text_2 = 'algo assustador, será que vai ficar tudo bem?"'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 4:
            dialogo_1_1 = 'Eu também filha'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Ela não gostaria que'
            dialogo_2_2 = 'ficássemos tristes'
            
            dialogo_3_1 = 'Você não deveria pensar nisso,'
            dialogo_3_2 = 'ja falamos disso'
            
            text_1 = '"Aida sim é bem chato falar disso, já que a mamãe morreu de covid no inicio do ano. Ainda tenho muitas'
            text_2 = 'saudades dela sabe"'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 5:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'De repente vocês ouvem um barulho vindo de dentro do posto. Você tenta enxergar algo la dentro mas, você esta'
            text_2 = 'muito longe e o interior muito escuro'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 6:
            dialogo_1_1 = 'Escolha uma opção: '
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Ir investigar'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Ir embora'
            dialogo_3_2 = ''
            
            text_1 = '"Papai estou com medo!"'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 7:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'O rádio deve ter te afetado um pouco, você decide parar de abastecer pra sair de onde estão e voltar para casa.'
            text_2 = 'Mas quando liga o carro, vê pessoas com a pele deformada e as bocas ensanguentadas saindo de dentro da loja'
            text_3 = 'e correndo em sua direção.'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 7.5:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ao ver isso, você liga o carro o mais rápido que consegue. Quando consegue engatar a primeira marcha '
            text_2 = 'é surpreendido quando uma dessas “pessoas” bate contra o seu vidro e outra contra o vidro no porta malas.'
            text_3 = 'Sem pensar duas vezes, você pisa fundo no acelerador escapa do posto'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        #Opção de ir investigar o posto começa
        elif contagem_txt == 8:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Instigado pelo barulho, você caminha em direção da porta e a abre. De imediato você fica completamente paralisado.'
            text_2 = 'Você se depara com duas pessoas em cima de um corpo com as entranha para fora. essas duas criaturas estão'
            text_3 = 'comendo o corpo no chão. A única reação instintiva que você consegue ter é correr dali. Você corre para o'
            text_4 = 'seu carro como nunca antes na vida.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #Acaba a investigação
        elif contagem_txt == 9:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você vê pessoas com a pele deformada e as bocas ensanguentadas saindo de dentro da loja e correndo em sua'
            text_2 = 'direção. Você liga o carro e o mais rapido que consegue mas, quando você consegue engatar a primeira você é'
            text_3 = 'surpreendido! Uma dessas "pessoas" bate contra o seu vidro quebrando-o. Sem pensar duas vezes, você pisa'
            text_4 = 'fundo no acelerador e escapa do posto.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 10:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Seguindo a instrução do aviso no rádio, você decide ir para sua xácara (uma pequena fazenda), podendo assim'
            text_2 = 'se afastar o maximo possivel da cidade'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 10.5: # mudar imagem para fazenda
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Chegando na sua fazenda, você e sua filha se trancam desesperadamente dentro de casa.'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 11:
            dialogo_1_1 = 'Eu não faço ideia'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Eram conservadores que'
            dialogo_2_2 = 'viram meu adesivo Liberal'
            
            dialogo_3_1 = 'Eram drogados que moravam ali'
            dialogo_3_2 = ''
            
            text_1 = '"PAI O QUE FOI AQUILO!?!"'
            text_2 = ''
            text_3 = ''
            text_4 = '(Você sente o desespero na voz de sua filha)'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 12:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Pai tem mais deles fora da casa, acho que seguiram o nosso carro!!'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 13:
            dialogo_1_1 = 'Sai da minha casa'
            dialogo_1_2 = 'ou eu atiro'
            
            dialogo_2_1 = 'Vocês que pediram'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Sempre quis atirar'
            dialogo_3_2 = 'esse bebe aqui'
            
            text_1 = 'Você lembra que tem uma 1911 9mm (pistola) guardada em caso de emergências. Você acredita que agora é uma'
            text_2 = 'emergência e pega ela, e depois se dirige para sua porta'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #minigame para introdução
        elif contagem_txt == 14:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Para andar com o personagem aperte as teclas AWSD, e para atirar as setas'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #rola minigame e fecha
        elif contagem_txt == 15:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Depois de despachar aquelas criaturas para as profundezas do inferno, você volta para a sua casa e barrica'
            text_2 = 'as portas e janelas. Após se acalmar um pouco, você liga a tv e o rádio e fica a espera de qualquer tipo'
            text_3 = 'de notícias do governo.'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 16:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = '1 ano se passou desde o incidente do posto. Esse tempo inteiro você e sua filha conseguiram sobreviver'
            text_2 = 'com os suprimentos que você mantinha em casa, mas ultimamente você percebe que eles estão acabando.'
            text_3 = 'Em uma manhã de domingo, você faz sua rotina diária de verificar a tv e o rádio. Como de costume só se'
            text_4 = 'escuta estática. Depois de algumas horas você é surpreendido com uma transmissão do rádio.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 17:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Aqui quem fala é o Coronel Marcus Fenix, das forças armadas dos Estados Unidos. Eu e meus homens estamos'
            text_2 = 'estacionados ao norte do Canada. Descobrimos que os infectados acabam morrendo em condiçõesde frio'
            text_3 = 'extremo. Assim, para qualquer um que essa mensagem possa encontrar, você terá um lugar aqui conosco'
            text_4 = 'Que Deus nos ajude nesses tempos difíceis e boa sorte a todos'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 18:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Depois de ouvir essa mensagem e notar a falta de suprimentos na sua casa, você tem uma ideia do que'
            text_2 = 'terá que fazer para sobreviver e faz um plano.'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 19:
            dialogo_1_1 = 'Sim, exatamene'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Isso se o carro chegar'
            dialogo_2_2 = 'ate o Canada'
            
            dialogo_3_1 = 'Você é surda? Não entendeu'
            dialogo_3_2 = 'na primeira vez?'
            
            text_1 = '"A gente vai fazer aquele plano mesmo? Vamos ir de carro ate o Canada para encontrar o Coronel'
            text_2 = 'coletando suprimentos ao longo do caminho?"'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 20:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Sua filha se lembrará disso'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 21:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Vocês entram no carro e partem rumo ao norte, a viajem é longa e árdua. Vocês passam horas dentro do'
            text_2 = 'carro, seguindo a rota que foi traçada no seu mapa. Vocês passaram direto pela cidade onde moravam,'
            text_3 = 'pois depois de um ano, já não sobrou basicamente nenhum suprimento para se pegar.' 
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 22:
            dialogo_1_1 = 'Escolha uma opção:'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Entrar na casa'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Continuar o caminho'
            dialogo_3_2 = ''
            
            text_1 = 'Apos 4 horas dirigindo pela estrada, rumo ao norte, você se depara com uma casa ao lado da estrada.'
            text_2 = 'Parece que você pode parar o carro e ver se há alguns suprimentos lá, mas sabe que se for há uma chance'
            text_3 = 'de uma horda de infectados alcançar você e sua filha. Mas ter suprimentos sempre é uma necessidade'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #entrou na casa
        elif contagem_txt == 23:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você estaciona o carro perto da casa e caminha na direção da mesma, chegando perto da estrutura,'
            text_2 = 'você vai percebendo seus detalhes. Mesmo que só tenha passado um ano desde o incidente, a falta'
            text_3 = 'de cuidado é notável. A pintura esta toda desbotada, com infiltrações e fungos por toda parte,'
            text_4 = 'se é tão ruim do lado de fora, você nem se atreve a imaginar como é dentro.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 24:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Indo contra seus instintos, você adentra aquela carcaça que um dia foi uma casa. Ao entrar o'
            text_2 = 'cheiro de mofo misturado com ar húmido atinge seu rosto, confirmando que o interior era tão ruim'
            text_3 = 'quanto o exterior. Mesmo assim, você aguenta essas condições para explorar a casa meticulosamente.'
            text_4 = 'No final da sua exploração, você ouve barulhos vindo de fora, logo percebe que uma horda alcançou'
            text_5 = 'vocês, mas sabe que pelo barulho não são muitos. Você deve se defender, pelo bem da sua filha.'
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #minigame rolando
        elif contagem_txt == 25:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Conseguiu! Você não sabe se foi seu amor pela sua filha ou sua pura raiva e odio pelas criaturas,'
            text_2 = 'mas no final você conseguiu. Sobreviveu à horda. Depois de tomar alguns segundos para recuperar'
            text_3 = 'seu fôlego, se dirige para seu carro e continua sua jornada ao norte com sua filha.'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #Sai da casa
        elif contagem_txt == 26:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você continua a viajem que é longa e, de certa forma, entediante. Vocês passam por cidades e fazendas,'
            text_2 = 'mas nenhuma parece ter alguma coisa que valesse a pena se arriscar. Todos esses edifícios destruídos'
            text_3 = 'pelo tempo e pelas hordas mostram a mórbida realidade que você e sua filha vivem. O mundo que um dia'
            text_4 = 'conheciam se foi, no seu lugar ficou apenas memórias de tempos pacíficos e simples.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 27:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Quanto mais você pensa nisso, mais vai notando o quanto pouco valor você dava para as coisas antes.'
            text_2 = 'Mesmo se os estresses do trabalho eram algo que ainda dão dor de cabeça ao se lembrar, percebe que'
            text_3 = 'nunca teve que se preocupar tanto na sobrevivência sua ou da sua filha. Nunca teve que se preocupar'
            text_4 = 'se ia ter comida pra vocês pro dia seguinte, ou se iam viver para passar fome. Isso tudo parece'
            text_5 = 'um pesadelo psicadélico, uma piada sem gosto, ou ate um filme cliché. Mas por mais que odeie'
            text_6 = 'isso, sua situação não é uma que possa ser acordada. O melhor que pode fazer agora é lidar com essa'
            text_7 = 'situação, já que a sua sobrevivência e da sua filha depende de VOCÊ.'
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 28:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Dias se passaram, e vocês ainda estão na estrada. Você não sabe quantos dias se passaram, 3...'
            text_2 = 'ou talvez 4. De qualquer forma você percebe pela neve que estão chegando ao norte, porem os'
            text_3 = 'seus suprimentos estão baixos... muito baixos. Você se questiona mais quanto tempo vocês conseguem'
            text_4 = 'seguir com os suprimentos que tem.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 29:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Se passaram algumas horas enquanto dirigia, quando você se depara com uma pequena cidade.'
            text_2 = 'Ela aparenta abandonada, mas só consegue ver dois edifícios em boas condições, uma loja de armas'
            text_3 = 'e uma loja de conveniência'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 30:
            dialogo_1_1 = 'Escolha uma opção:'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Explorar a loja de armas'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Explorar a loja de'
            dialogo_3_2 = 'conveniência'
            
            text_1 = '"Papai, eu to com muita fome... e com frio"'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 31:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você da preferência á proteção de vocês dois. Afinal, passar um pouco de fome não mata ninguém,mas os'
            text_2 = 'infectados sim. Você estaciona o carro próximo da loja para poder explora-la. A lojaaparenta estar'
            text_3 = 'em boas condições... para os padrões dos dias de hoje. Como esperado o lugar já foi saqueda'
            text_4 = 'antes, ainda sim você checa para ver se sobrou alguma munição. Você decide checar atras do'
            text_5 = 'balcão, geralmente é guardado algumas balas para os funcionários da loja (para proteção claro).'
            text_6 = 'BAZINGA! Ainda bem que ninguém checa atras do balcão, conseguiu achar algumas balas para sua pistola'
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 32:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você da preferência á saúde da sua filha (e sua no processo). Ver sua filha ter que passar fome é'
            text_2 = 'algo que nenhum pai deveria, já que isso afeta seu coração e sua mente, afinal essa jornada é pelo'
            text_3 = 'bem e sobrevivência dela. A loja aparenta estar em boas condições para os padrões dos dias de hoje.'
            text_4 = 'Como esperado o lugar já foi saqueado antes, ainda sim você checa para ver se sobrou alguma comida.'
            text_5 = 'Você decide checar nos galpões do fundo, geralmente é guardado alguns alimentos não perecíveis lá.'
            text_6 = 'BOSTA! Não sobrou nada... nem um pedacinho de nada.'
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 33:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'No final da sua exploração da loja, você houve barulhos de passos vindo de fora. Você até'
            text_2 = 'acharia que eram pessoas se não fosse o cheiro pútrido vindo da direção dos passos.'
            text_3 = '‘Mais infectados para mandar pro inferno’: você pensa enquanto prepara sua arma'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #minigame da loja de armas rolando
        elif contagem_txt == 34:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Novamente você mostra para as criaturas o porque você esta vivo a tanto tempo.'
            text_2 = 'Sobrevivendo mais uma horda, você volta para seu carro com mais balas do que tinha antes.'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 35:
            dialogo_1_1 = 'Infelizmente não docinho, aguenta'
            dialogo_1_2 = 'mais um pouquinho, okay?'
            
            dialogo_2_1 = 'Não docinho, mas o papai vai'
            dialogo_2_2 = 'proteger melhor a gente, okay?'
            
            dialogo_3_1 = 'Não, mas você ficar enchendo'
            dialogo_3_2 = 'o saco do papai não ajuda, okay?'
            
            text_1 = '"Papai, você ta bem! Fiquei preocupada, aqueles monstros apareceram do nada.'
            text_2 = 'Então... conseguiu um pouco mais de comida?"'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 36:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ela se lembrará disso'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 37:
            dialogo_1_1 = 'Escolha uma opção:'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Explorar o posto abandonado'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Continuar viajem'
            dialogo_3_2 = ''
            
            text_1 = 'Vocês continuam dirigindo em direção ao norte por algumas horas pela estrada. Der repente, no canto'
            text_2 = 'da estrada, você avista um posto de gasolina que aparenta estar abandonado. A condição do posto'
            text_3 = 'esta, surpreendentemente, descente'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 38:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você estaciona seu carro perto do posto. Antes de entrar, você verifica se consegue detectar'
            text_2 = 'alguma horda de infectados... não ouve nada, então você entra no posto para saquear.Você não'
            text_3 = 'acha muita coisa, só algumas balas para sua arma e um pouco de comida, além de combustível'
            text_4 = 'para o seu carro. Você então volta para o seu carro e continua sua viajem'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 39:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Se passaram alguns dias desde a última parada, porém algo chama sua atenção. Logo a frente'
            text_2 = 'está uma grande cidade. Esta cidade não possui a mesma vida de antes, ela parece vazia.'
            text_3 = 'Devido as circunstancias você se sente forçado a entrar nas entranhas da cidade para'
            text_4 = 'procurar suprimentos.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 40:
            dialogo_1_1 = 'Do que voces estão falando?'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Quem são voces?'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Nao se aproxime do carro!!'
            dialogo_3_2 = ''
            
            text_1 = 'A rua esta bloqueada, voce para o caro e logo dois homens aparecem e se aproximam do carro e um deles grita'
            text_2 = ''
            text_3 = '“Oi, Oi, voce veio em busca de Alexandria?”'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 41:
            dialogo_1_1 = 'quem se importa com a'
            dialogo_1_2 = 'colonia de voces!'
            
            dialogo_2_1 = 'Nos estamos indo para'
            dialogo_2_2 = 'o Canada'
            
            dialogo_3_1 = 'Já falei pra não se'
            dialogo_3_2 = 'aproximar do carro!'
            
            text_1 = '"Relaxa senhor, nos estamos em busca de mais sobreviventes para nossa cidade, queremos recrutar para a colonia"'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 42:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ele se lembrará disso'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 43:
            dialogo_1_1 = 'Não temos escolha'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Eles parecem ser gente boa'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Cala a boca, quem manda'
            dialogo_3_2 = 'aqui sou eu'
            
            text_1 = '"bom, mesmo que voce nao queira se juntar a nos, poderia nos ajudar a coletar suprimentos'
            text_2 = 'aqui perto? Te daremos uma parte"'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = 'Pai, n temos mais suprimentos, mas sera que podemos confiar neles?'
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 44:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ela se lembrará disso'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 45:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você ve seu estoque em 0 e percebe que é obrigado a se juntar com eles para procurar por'
            text_2 = 'suprimentos, voce para o carro ali mesmo tira a chaves e vai com os homems'
            text_3 = ''
            text_4 = 'Não longe dali voce se depara com uma loja de conveniencia, e entao o homem com quem você'
            text_5 = 'tinha conversado aponta para lá'
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 46:
            dialogo_1_1 = 'Eu tenho filha'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Vocês que me chamaram vão vocês'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Não prescisa falar duas vezes'
            dialogo_3_2 = ''
            
            text_1 = '"Você primeiro! Eu to quase sem muniçao, não vou te ajudar muito"'
            text_2 = ''
            text_3 = '"Diz o homem com quem você tem falado até agora"'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 47:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Você vai na frente e abre a porta da mercearia, voce sente o cheiro de carne podre,'
            text_2 = 'normal dos zumbies e entao vc escuta um grunido vindo na sua direçao'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #minigame rolando
        elif contagem_txt == 48:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Todos entram na mercearia e começam a procurar por suprimentos.'
            text_2 = 'De repente você escuta um grito de um homem e um grande barulho vindo do fundo da loja, você '
            text_3 = 'corre lá e um dos homems que estavam com você esta mordido e e o outro esta totalmente em choque'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 50:
            dialogo_1_1 = 'Como voce pode fazer isso?'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Belo tiro'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Você esta insano?'
            dialogo_3_2 = ''
            
            text_1 = 'Você ve esse homem atirando no amigo dele, e se assusta'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 51:
            dialogo_1_1 = 'Mas deixe ele se tranformar primeiro'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Então alexandria é um campo de'
            dialogo_2_2 = 'massacres'
            
            dialogo_3_1 = 'Isso foi muito desumano'
            dialogo_3_2 = ''
            
            text_1 = '"Ele foi mordido, depois disso não tem mais volta, é so questão de tempo até ele virar um zumbie.'
            text_2 = 'Aquelas pesquisas primarias não eram conclusivas, a gente tirou essa conclusão depois que'
            text_3 = 'isso aconteceu diversas vezes"'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 52:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = '"Nenhum de nos quer virar uma dessas coisas, é uma das regras de Alexandria, se fomos mordidos,'
            text_2 = 'a lei diz que podemos atirar"'
            text_3 = ''
            text_4 = ''
            text_5 = 'Quando ele fala isso voces escutam um baruho alto vindo da parte da frente da loja, quando vão checar'
            text_6 = 'varios zumbies estao na frente da loja tentando entrar'
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 53:
            dialogo_1_1 = 'Solta ela seu filho de uma puta'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Ela é a unica familia que me'
            dialogo_2_2 = 'resta por favor'
            
            dialogo_3_1 = 'Eu sabia que voces nao eram'
            dialogo_3_2 = 'pessoas boas'
            
            text_1 = 'Do nada, aquele homem que estava com você aponta a arma para sua filha e diz'
            text_2 = '“Me de toda sua munição”'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 54:
            dialogo_1_1 = 'Calma cara relaxa, tudo'
            dialogo_1_2 = 'vai dar certo'
            
            dialogo_2_1 = 'Solta ela agora poha'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Eu te dou metade das'
            dialogo_3_2 = 'minhas muniçoes'
            
            text_1 = '“Escuta cara, eu tenho familia também, duas filhas e uma esposa, eu tenho que voltar para elas”'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 55:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = '"Me da tudo agora!! O tempo esta acabando vai logo"'
            text_2 = ''
            text_3 = 'Quando ele fala isso um zumbie vem por tras dele e morde ele, que o faz soltar sua filha'
            text_4 = 'O zumbi cai por cima dele e quando isso aconteve os outros zumbies que estavam na frente da loja entram'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #minigame rolando
        elif contagem_txt == 56:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Um zumbi que você não tinha visto te ataca por trás e acaba mordendo seu braço, sua filha queestava focada'
            text_2 = 'em outros zumbies não ve você sendo mordido'
            text_3 = ''
            text_4 = ''
            text_5 = '”Vamos embora pai”'
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 57:
            dialogo_1_1 = 'Fica quieta menina'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Sim...'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Nunca estive melhor'
            dialogo_3_2 = ''
            
            text_1 = 'Vocês estão correndo pela rua vazia em direçao ao carro'
            text_2 = ''
            text_3 = '“Você esta bem pai? Esta muito palido!”'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 58:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ela se lembrará disso'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 59:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = ''
            text_2 = 'Vocês continuam correndo e estão quase no carro, quando você sente seu corpo ficar leve e cai no chão'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 60:
            dialogo_1_1 = 'Cuida da sua vida'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Não se preocupe comigo'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Vamos rapido!'
            dialogo_3_2 = ''
            
            text_1 = '"Pai com certeza você não está bem!'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 61:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ela se lembrará disso'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 62:
            dialogo_1_1 = 'Eu não sei se consigo continuar'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Será que eu estou me'
            dialogo_2_2 = 'transformando em um deles?'
            
            dialogo_3_1 = 'Estou bem so presciso descancar'
            dialogo_3_2 = ''
            
            text_1 = 'Você sente que está perdendo controle do seu corpo, e que logo se tornará um zumbi'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 63:
            dialogo_1_1 = 'Eu fui mordido'
            dialogo_1_2 = ''
            
            dialogo_2_1 = '*mostrar mordida*'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Aconteceu na loja,'
            dialogo_3_2 = 'foi muito rapido'
            
            text_1 = '"Pai do que o senhor está falando?"'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 64:
            dialogo_1_1 = 'Está tudo bem, mas você terá'
            dialogo_1_2 = 'que continuar sem mim'
            
            dialogo_2_1 = 'Eu nao quero me tornar um deles'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Eu vou morrer'
            dialogo_3_2 = ''
            
            text_1 = '"Meu Deus! O que faremos agora!?!"'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 65:
            dialogo_1_1 = 'Você tem que ir embora e me deixar'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Saia daqui, vai embora'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Por favor filha não me deixe'
            dialogo_3_2 = 'virar um deles'
            
            text_1 = 'Eu não vou te abandonar!'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #COntinua com resposta 1 e 2
        elif contagem_txt == 66:
            if contagem_filha <= 3:
                dialogo_1_1 = 'Você tem que fazer isso,'
                dialogo_1_2 = 'é pelo seu bem'
            
                dialogo_2_1 = 'Voce é forte, sempre foi,'
                dialogo_2_2 = 'voce tem que fazer isso'
            
                dialogo_3_1 = 'Vai logo filha'
                dialogo_3_2 = ''
            
                text_1 = 'Sua filha começa a chorar'
                text_2 = ''
                text_3 = ''
                text_4 = ''
                text_5 = ''
                text_6 = ''
                text_7 = ''
                text_8 = ''
                text_9 = ''
            else:
                dialogo_1_1 = ' ... '
                dialogo_1_2 = ''
            
                dialogo_2_1 = ' poxa ...'
                dialogo_2_2 = ''
            
                dialogo_3_1 = '... Adeus'
                dialogo_3_2 = ''
            
                text_1 = '"Está bem, até nunca mais velhote"'
                text_2 = ''
                text_3 = ''
                text_4 = ''
                text_5 = ''
                text_6 = ''
                text_7 = ''
                text_8 = ''
                text_9 = ''
        elif contagem_txt == 67:
            dialogo_1_1 = 'Lembre-se, nunca olhe'
            dialogo_1_2 = 'para tras'
            
            dialogo_2_1 = 'Eu te amo filha'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Nunca se esqueça de mim'
            dialogo_3_2 = ''
            
            text_1 = 'Você ve sua filha indo de costas para você, e ela vai se afastando, ela vira, da um sorriso e vai embora'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 68:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Ela te da uma ultima olhada e segue ate sumir da sua vista, você sabe que nunca vão se ver novamente'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #fim da escolha da resposta 1 e 2
            #Escolha de sua filha te matar
        elif contagem_txt == 69:
            dialogo_1_1 = 'Sim'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Pega minha pistola'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'vai rapido por favor'
            dialogo_3_2 = ''
            
            text_1 = 'O que? Você quer que eu te mate!?!'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        elif contagem_txt == 70:
            if contagem_filha <= 3:
                dialogo_1_1 = '*dar a pistola*'
                dialogo_1_2 = ''
            
                dialogo_2_1 = 'Boa filha'
                dialogo_2_2 = ''
            
                dialogo_3_1 = 'Te amo'
                dialogo_3_2 = ''
                
                text_1 = 'Ta bom, eu faço isso'
                text_2 = ''
                text_3 = ''
                text_4 = ''
                text_5 = ''
                text_6 = ''
                text_7 = ''
                text_8 = ''
                text_9 = ''
            else:
                dialogo_1_1 = 'Você tem que fazer isso'
                dialogo_1_2 = ''
            
                dialogo_2_1 = 'Eu te amo'
                dialogo_2_2 = ''
            
                dialogo_3_1 = '*dar a pistola*'
                dialogo_3_2 = ''
                
                text_1 = '"Eu não vou fazer isso!!"'
                text_2 = ''
                text_3 = 'Sua filha chora intensamente'
                text_4 = ''
                text_5 = ''
                text_6 = ''
                text_7 = ''
                text_8 = ''
                text_9 = ''
        elif contagem_txt == 71:
            dialogo_1_1 = 'Lembre-se, nunca olhe'
            dialogo_1_2 = 'para tras'
            
            dialogo_2_1 = 'Eu te amo filha'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Nunca se esqueça de mim'
            dialogo_3_2 = ''
            
            text_1 = 'Ela pega sua pistola e poe a mira na sua cabeça, ela treme muito'
            text_2 = ''
            text_3 = '"Adeus"'
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #acaba 
            #final
        elif contagem_txt == 72:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Sua filha agora esta em um grupo de 6 pessoas, todos estao indo para o Canada'
            text_2 = 'Ela se lembra de voce todos os dias mas nao chora mais, ela se tornou muito mais forte e resiliente'
            text_3 = 'Agora ela encontrou pessoas que ela pode chamar de familia, e se tornou alguem feliz novamente'
            text_4 = 'Apos dois anos eles finalmente chegam a uma grande muralha em meio a uma tempestade de neve, e no'
            text_5 = 'portao tem um escrito “Le resistence"'
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #acabou
        elif contagem_txt == 73:
            dialogo_1_1 = 'Escolha um dos dois:'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Restart game'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Quit game'
            dialogo_3_2 = ''
            
            text_1 = '"THE END"'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        
        all_sprites.update()
        #formula para fazer a imagem linha 97
        if contagem_txt == 0:
            window.fill(BLACK)
            window.blit(recursos['teste'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 1:
            window.fill(BLACK)
            window.blit(recursos['1'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 2:
            window.fill(BLACK)
            window.blit(recursos['2'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 3 and contagem_txt < 5:
            window.fill(BLACK)
            window.blit(recursos['3'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >=5 and contagem_txt < 7:
            window.fill(BLACK)
            window.blit(recursos['4'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 8:
            window.fill(BLACK)
            window.blit(recursos['5'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 7 or contagem_txt == 7.5:
            window.fill(BLACK)
            window.blit(recursos['6'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 9:
            window.fill(BLACK)
            window.blit(recursos['7'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 10:
            window.fill(BLACK)
            window.blit(recursos['8'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 10.5:
            window.fill(BLACK)
            window.blit(recursos['9'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 11:
            window.fill(BLACK)
            window.blit(recursos['10'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 12 and contagem_txt < 15:
            window.fill(BLACK)
            window.blit(recursos['11'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 15 and contagem_txt < 19:
            window.fill(BLACK)
            window.blit(recursos['12'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 19 and contagem_txt < 21:
            window.fill(BLACK)
            window.blit(recursos['13'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 21:
            window.fill(BLACK)
            window.blit(recursos['14'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 22 and contagem_txt < 26:
            window.fill(BLACK)
            window.blit(recursos['15'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 26 and contagem_txt < 29:
            window.fill(BLACK)
            window.blit(recursos['16'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 29:
            window.fill(BLACK)
            window.blit(recursos['17'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 30:
            window.fill(BLACK)
            window.blit(recursos['18'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 31:
            window.fill(BLACK)
            window.blit(recursos['19'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 32:
            window.fill(BLACK)
            window.blit(recursos['20'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 33 and contagem_txt < 37:
            window.fill(BLACK)
            window.blit(recursos['21'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 37:
            window.fill(BLACK)
            window.blit(recursos['22'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 38:
            window.fill(BLACK)
            window.blit(recursos['23'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 39:
            window.fill(BLACK)
            window.blit(recursos['24'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 40 and contagem_txt < 46:
            window.fill(BLACK)
            window.blit(recursos['25'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 46:
            window.fill(BLACK)
            window.blit(recursos['26'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 47:
            window.fill(BLACK)
            window.blit(recursos['27'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 48:
            window.fill(BLACK)
            window.blit(recursos['28'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 50 and contagem_txt < 53:
            window.fill(BLACK)
            window.blit(recursos['29'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 53 and contagem_txt < 55:
            window.fill(BLACK)
            window.blit(recursos['30'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 55:
            window.fill(BLACK)
            window.blit(recursos['31'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 56:
            window.fill(BLACK)
            window.blit(recursos['32'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 57 and contagem_txt < 59:
            window.fill(BLACK)
            window.blit(recursos['33'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt >= 60 and contagem_txt < 72:
            window.fill(BLACK)
            window.blit(recursos['34'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 72:
            window.fill(BLACK)
            window.blit(recursos['35'], (0, 0))
            all_sprites.draw(window)
        elif contagem_txt == 73:
            window.fill(BLACK)
            window.blit(recursos['36'], (0, 0))
            all_sprites.draw(window)
            
# GAME OVER
#        elif contagem_txt <= 72:
#            window.fill(BLACK)
#            window.blit(recursos['36'], (0, 0))
#           all_sprites.draw(window)

        #ate aqui
        draw_text(window, dialogo_1_1, TEXT_SIZE, DIALOGO_WIDTH_1_1, DIALOGO_HEIGHT_1_1)
        draw_text(window, dialogo_1_2, TEXT_SIZE, DIALOGO_WIDTH_1_2, DIALOGO_HEIGHT_1_2)
        
        draw_text(window, dialogo_2_1, TEXT_SIZE, DIALOGO_WIDTH_2_1, DIALOGO_HEIGHT_2_1)
        draw_text(window, dialogo_2_2, TEXT_SIZE, DIALOGO_WIDTH_2_2, DIALOGO_HEIGHT_2_2)

        draw_text(window, dialogo_3_1, TEXT_SIZE, DIALOGO_WIDTH_3_1, DIALOGO_HEIGHT_3_1)
        draw_text(window, dialogo_3_2, TEXT_SIZE, DIALOGO_WIDTH_3_2, DIALOGO_HEIGHT_3_2)

        draw_text(window, text_1, TEXT_SIZE, TEXTO_WIDTH_1, TEXTO_HEIGHT_1)
        draw_text(window, text_2, TEXT_SIZE, TEXTO_WIDTH_2, TEXTO_HEIGHT_2)
        draw_text(window, text_3, TEXT_SIZE, TEXTO_WIDTH_3, TEXTO_HEIGHT_3)
        draw_text(window, text_4, TEXT_SIZE, TEXTO_WIDTH_4, TEXTO_HEIGHT_4)
        draw_text(window, text_5, TEXT_SIZE, TEXTO_WIDTH_5, TEXTO_HEIGHT_5)
        draw_text(window, text_6, TEXT_SIZE, TEXTO_WIDTH_6, TEXTO_HEIGHT_6)
        draw_text(window, text_7, TEXT_SIZE, TEXTO_WIDTH_7, TEXTO_HEIGHT_7)
        draw_text(window, text_8, TEXT_SIZE, TEXTO_WIDTH_8, TEXTO_HEIGHT_8)
        draw_text(window, text_9, TEXT_SIZE, TEXTO_WIDTH_9, TEXTO_HEIGHT_9)
        
        pygame.display.update()
        
tela_jogo(window)
    
pygame.quit()
