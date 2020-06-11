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
    
    recursos['posto_gasolina_1'] = pygame.image.load('imgs/1.png').convert()
    
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
                print(px)
                print(py)
                if contagem_txt == 1:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 2
                        
                elif contagem_txt == 2:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 3
                        
                elif contagem_txt == 3:
                    if px > 16 and px < 266 and py > 590 and py < 520:
                        
                        contagem_txt = 4
                    
                    elif px > 277 and px < 523 and py > 590 and py < 520:
                        
                        contagem_txt = 4
                    
                    elif px > 537 and px < 784 and py > 590 and py < 520:
                        
                        contagem_txt = 4
                
                elif contagem_txt == 4:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                        game = False
                        
        if contagem_txt == 1:
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
        if contagem_txt == 2:
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
        if contagem_txt == 3:
            dialogo_1_1 = 'Claro, vai ficar tudo bem'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Essa midia é muito fantasiosa,'
            dialogo_2_2 = 'tao inventando coisa'
            
            dialogo_3_1 = 'Eu sinceramente não sei docinho'
            dialogo_3_2 = ''
            
            text_1 = 'Nossa pai, ainda abem que o senhor não é pró Trump e não fomos tomar a cloroquina, mas o rádio falou '
            text_2 = 'algo assustador, será que vai ficar tudo bem?'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 4:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = ''
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''

        
        all_sprites.update()
        
        window.fill(BLACK)
        window.blit(recursos['posto_gasolina_1'], (0, 0))
        all_sprites.draw(window)
        
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

