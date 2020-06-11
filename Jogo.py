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
                    
                    #elif px > 277 and px < 523 and py > 590 and py < 520:
                        
                   #     contagem_txt = 4
                    
                    #elif px > 537 and px < 784 and py > 590 and py < 520:
                        
                     #   contagem_txt = 4
                
              #  elif contagem_txt == 4:
               #     if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                        
                #Aumenta o contador do texto para mudar o que aparece escrito
                elif contagem_txt == 4:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 5
                         
                elif contagem_txt == 5:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:

                        contagem_txt = 6
                        
                elif contagem_txt == 6:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 7
                         
                elif contagem_txt == 7:
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
                        
                         contagem_txt = 11
                
                elif contagem_txt == 11:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 12
                         
                elif contagem_txt == 12:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 13
                        
                elif contagem_txt == 13:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 14
                         
                elif contagem_txt == 14:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 15
                         
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
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 20

                elif contagem_txt == 20:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 21
                         
                elif contagem_txt == 21:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 22
                         
                elif contagem_txt == 22:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 23
                         
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
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 31 
                
                elif contagem_txt == 31:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 32
                         
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
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 36
                         
                elif contagem_txt == 36:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 37
                         
                elif contagem_txt == 37:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 38
                         
                elif contagem_txt == 38:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 39
                         
                elif contagem_txt == 39:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 40
                        
                elif contagem_txt == 40:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 41
                         
                elif contagem_txt == 41:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 42 
                         
                elif contagem_txt == 42:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 43
                         
                elif contagem_txt == 43:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 44
                         
                elif contagem_txt == 44:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 45
                         
                elif contagem_txt == 45:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 46
                         
                elif contagem_txt == 46:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 47
                        
                elif contagem_txt == 47:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 48
                         
                elif contagem_txt == 48:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 49
                         
                elif contagem_txt == 49:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 50
                         
                elif contagem_txt == 50:
                    if px > 0 and px < WIDTH and py > 0 and py < HEIGHT:
                        
                         contagem_txt = 51
                         
                         game = False
                         
            
        #Todas as falas e textos do jogo                
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
            dialogo_1_1 = 'Eu também filha'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Ela não gostaria que'
            dialogo_2_2 = 'ficássemos tristes'
            
            dialogo_3_1 = 'Você não deveria pensar nisso'
            dialogo_3_2 = ''
            
            text_1 = 'Aida sim é bem chato falar disso, já que a mamãe morreu de covid no inicio do ano. Ainda tenho muitas'
            text_2 = 'saudades dela sabe'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 5:
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
        if contagem_txt == 6:
            dialogo_1_1 = 'Ir investigar'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Ir embora'
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Papai estou com medo!'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #Opção de ir investigar o posto começa
        if contagem_txt == 8:
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
        if contagem_txt == 9:
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
        if contagem_txt == 10:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Seguindo a instrução do aviso no rádio, você decide ir para sua xácara (uma pequena fazenda), podendo assim'
            text_2 = 'se afastar o maximo possivel da cidade'
            text_3 = ''
            text_4 = 'Chegando na sua fazenda, você e sua filha se trancam desesperadamente dentro de casa.'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 11:
            dialogo_1_1 = 'Eu não faço ideia'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Eram conservadores que'
            dialogo_2_2 = 'viram meu adesivo Liberal'
            
            dialogo_3_1 = 'Eram drogados que moravam ali'
            dialogo_3_2 = ''
            
            text_1 = 'PAI O QUE FOI AQUILO!?!'
            text_2 = ''
            text_3 = ''
            text_4 = '(Você sente o desespero na voz de sua filha)'
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 12:
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
        if contagem_txt == 13:
            dialogo_1_1 = 'Sai da minha casa'
            dialogo_1_2 = 'ou eu atiro'
            
            dialogo_2_1 = 'Vocês que pediram'
            dialogo_2_2 = ''
            
            dialogo_3_1 = 'Sempre quis atirar'
            dialogo_3_2 = ''
            
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
        if contagem_txt == 14:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Para andar com o personagem aperte AWSD, e para atirar as setas'
            text_2 = ''
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
            #rola minigame e fecha
        if contagem_txt == 15:
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
        if contagem_txt == 16:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = '1 ano se passou desde o incidente do posto. Esse tempo inteiro você e sua filha conseguiram sobreviver'
            text_2 = 'com os suprimentos que você mantinha em casa, mas ultimamente você percebe que eles estão acabando.'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 17:
            dialogo_1_1 = ''
            dialogo_1_2 = ''
            
            dialogo_2_1 = ''
            dialogo_2_2 = ''
            
            dialogo_3_1 = ''
            dialogo_3_2 = ''
            
            text_1 = 'Em uma manhã de domingo, você faz sua rotina diária de verificar a tv e o rádio. Como de costume só se'
            text_2 = 'escuta estática. Depois de algumas horas você é surpreendido com uma transmissão do rádio.'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 18:
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
        if contagem_txt == 19:
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
        if contagem_txt == 20:
            dialogo_1_1 = 'Sim, exatamene'
            dialogo_1_2 = ''
            
            dialogo_2_1 = 'Isso se o carro chegar'
            dialogo_2_2 = 'ate o Canada'
            
            dialogo_3_1 = 'Você é surda? Não entendeu'
            dialogo_3_2 = 'na primeira vez?'
            
            text_1 = 'A gente vai fazer aquele plano mesmo? Vamos ir de carro ate o Canada para encontrar o Coronel'
            text_2 = 'coletando suprimentos ao longo do caminho?'
            text_3 = ''
            text_4 = ''
            text_5 = ''
            text_6 = ''
            text_7 = ''
            text_8 = ''
            text_9 = ''
        if contagem_txt == 21:
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
        if contagem_txt == 22:
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
        if contagem_txt == 23:
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
        if contagem_txt == 24:
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
        if contagem_txt == 25:
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
        if contagem_txt == 26:
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
        if contagem_txt == 27:
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
        if contagem_txt == 28:
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
        if contagem_txt == 29:
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
        if contagem_txt == 30:
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
        if contagem_txt == 31:
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
        if contagem_txt == 32:
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
        if contagem_txt == 33:
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
        if contagem_txt == 34:
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
        if contagem_txt == 35:
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
        if contagem_txt == 36:
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
        if contagem_txt == 37:
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
        if contagem_txt == 38:
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
        if contagem_txt == 39:
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
        if contagem_txt == 40:
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
        if contagem_txt == 41:
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
        if contagem_txt == 42:
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
        if contagem_txt == 43:
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
        if contagem_txt == 44:
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
        if contagem_txt == 45:
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
        if contagem_txt == 46:
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
        if contagem_txt == 47:
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
        if contagem_txt == 48:
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
        if contagem_txt == 49:
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
        if contagem_txt == 50:
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

