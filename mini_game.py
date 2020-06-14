# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 17:05:16 2020

@author: pedro
"""
# Importa para usar os recursos
import pygame
import random

pygame.init()
pygame.mixer.init()

# Criando a tela do jogo

WIDTH = 800
HEIGHT = 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mini_game')

# Cria os recursos do minigame

FPS = 30
ZOMBIE_WIDTH = 120
ZOMBIE_HEIGHT = 100
SURVIVOR_WIDTH = 50
SURVIVOR_HEIGHT = 38
BALA_WIDTH = 15
BALA_HEIGTH = 20

def load_dic_recursos():
    dic_recursos = {}

    dic_recursos['fundo'] = pygame.image.load('img/background_prototipo.png').convert()
    dic_recursos['fundo'] = pygame.transform.scale(dic_recursos['fundo'], (WIDTH, HEIGHT))
    dic_recursos['zombie_img'] = pygame.image.load('img/zombie_prototipo.png').convert_alpha()
    dic_recursos['zombie_img'] = pygame.transform.scale(dic_recursos['zombie_img'], (ZOMBIE_WIDTH, ZOMBIE_HEIGHT))
    dic_recursos['sobrevivente_img'] = pygame.image.load('img/Player_test1.png').convert_alpha()
    dic_recursos['sobrevivente_img'] = pygame.transform.scale(dic_recursos['sobrevivente_img'], (SURVIVOR_WIDTH, SURVIVOR_HEIGHT))
    dic_recursos['tiro_1'] = pygame.image.load('img/tiro_cima.png').convert_alpha()
    dic_recursos['tiro_1'] = pygame.transform.scale(dic_recursos['tiro_1'], (BALA_WIDTH, BALA_HEIGTH))

    dic_recursos['tiro_2'] = pygame.image.load('img/tiro_baixo.png').convert_alpha()
    dic_recursos['tiro_2'] = pygame.transform.scale(dic_recursos['tiro_2'], (BALA_WIDTH, BALA_HEIGTH))

    dic_recursos['tiro_3'] = pygame.image.load('img/tiro_direita.png').convert_alpha()
    dic_recursos['tiro_3'] = pygame.transform.scale(dic_recursos['tiro_3'], (BALA_WIDTH, BALA_HEIGTH))

    dic_recursos['tiro_4'] = pygame.image.load('img/tiro_esquerda.png').convert_alpha()
    dic_recursos['tiro_4'] = pygame.transform.scale(dic_recursos['tiro_4'], (BALA_WIDTH, BALA_HEIGTH))
    
    # Animação da morte

    sangue_anim = []
    for i in range(4):
        arquivo = 'img/sangue_img0{}.png'.format(i)
        anim = pygame.image.load(arquivo).convert()
        anim = pygame.transform.scale(anim, (40, 40))
        sangue_anim.append(anim)
    dic_recursos["sangue_anim"] = sangue_anim
    
    return dic_recursos

# Criando as classes

#       Zombies
class Zombie(pygame.sprite.Sprite):
    def __init__(self, dic_recursos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = dic_recursos['zombie_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - ZOMBIE_WIDTH)
        self.rect.y = random.randint(-100, - ZOMBIE_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # recoloca os zombies na tela quando eles sairem
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH - ZOMBIE_WIDTH)
            self.rect.y = random.randint(-100, - ZOMBIE_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)

#       Tiro         
#       Tiro para cima
class Bullet_1(pygame.sprite.Sprite):
    def __init__(self, dic_recursos, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = dic_recursos['tiro_1']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = - 30  # Velocidade para cima

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()

#       Tiro para baixo
class Bullet_2(pygame.sprite.Sprite):
    def __init__(self, dic_recursos, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = dic_recursos['tiro_2']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedy = + 30  # Velocidade fixa para baixo

    def update(self):
        # A bala só se move no eixo y
        self.rect.y += self.speedy

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom > HEIGHT:
            self.kill()

#       Tiro para direita
class Bullet_3(pygame.sprite.Sprite):
    def __init__(self, dic_recursos, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = dic_recursos['tiro_3']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = + 30  # Velocidade fixa para direita

    def update(self):
        # A bala só se move no eixo x
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom > WIDTH:
            self.kill()

#       Tiro para esquerda
class Bullet_4(pygame.sprite.Sprite):
    def __init__(self, dic_recursos, bottom, centerx):
        pygame.sprite.Sprite.__init__(self)

        self.image = dic_recursos['tiro_4']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()

        self.rect.centerx = centerx
        self.rect.bottom = bottom
        self.speedx = - 30  # Velocidade fixa para esquerda

    def update(self):
        # A bala só se move no eixo y
        self.rect.x += self.speedx

        # Se o tiro passar do inicio da tela, morre.
        if self.rect.bottom < 0:
            self.kill()
            
#       sobrevivente
class Sobrevivente(pygame.sprite.Sprite):
    def __init__(self, groups, dic_recursos):
        pygame.sprite.Sprite.__init__(self)

        self.image = dic_recursos['sobrevivente_img']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0
        self.groups = groups
        self.dic_recursos = dic_recursos

        # Só será possível atirar uma vez a cada 500 milissegundos
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        # Atualização da posição do player
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        # Mantem dentro da tela
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def shoot_1(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet_1 = Bullet_1(self.dic_recursos, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet_1)
            self.groups['all_bullets_1'].add(new_bullet_1)

    def shoot_2(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet_2 = Bullet_2(self.dic_recursos, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet_2)
            self.groups['all_bullets_2'].add(new_bullet_2)
            
    def shoot_3(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet_3 = Bullet_3(self.dic_recursos, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet_3)
            self.groups['all_bullets_3'].add(new_bullet_3)
            
    def shoot_4(self):
        # Verifica se pode atirar
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde o último tiro.
        elapsed_ticks = now - self.last_shot

        # Se já pode atirar novamente...
        if elapsed_ticks > self.shoot_ticks:
            # Marca o tick da nova imagem.
            self.last_shot = now
            # A nova bala vai ser criada logo acima e no centro horizontal da nave
            new_bullet_4 = Bullet_4(self.dic_recursos, self.rect.top, self.rect.centerx)
            self.groups['all_sprites'].add(new_bullet_4)
            self.groups['all_bullets_4'].add(new_bullet_4)

# Classe da anim de morte
class Sangue(pygame.sprite.Sprite):
    def __init__(self, center, dic_recursos):
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de sangue
        self.sangue_anim = dic_recursos["sangue_anim"]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.sangue_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.sangue_anim):
                # Se sim, acaba a anim
                self.kill()
            else:
                # Se ainda não chegou ao fim da anim, troca de imagem.
                center = self.rect.center
                self.image = self.sangue_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    
    dic_recursos = load_dic_recursos()
    
    # Criando os grupos
    all_sprites = pygame.sprite.Group()
    all_zombies = pygame.sprite.Group()
    all_bullets_1 = pygame.sprite.Group()
    all_bullets_2 = pygame.sprite.Group()
    all_bullets_3 = pygame.sprite.Group()
    all_bullets_4 = pygame.sprite.Group()
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_zombies'] = all_zombies
    groups['all_bullets_1'] = all_bullets_1
    groups['all_bullets_2'] = all_bullets_2
    groups['all_bullets_3'] = all_bullets_3
    groups['all_bullets_4'] = all_bullets_4
    
    # Criando o jogador
    player = Sobrevivente(groups, dic_recursos)
    all_sprites.add(player)
    
    # Criando os zombies
    for i in range(8):
        zombie = Zombie(dic_recursos)
        all_sprites.add(zombie)
        all_zombies.add(zombie)

    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING
    
    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_a:
                        player.speedx -= 10

                    if event.key == pygame.K_d:
                        player.speedx += 10

                    if event.key == pygame.K_w:
                        player.speedy -= 10
  
                    if event.key == pygame.K_s:
                        player.speedy += 10
                
                    if event.key == pygame.K_UP:
                        player.shoot_1()
                    
                    if event.key == pygame.K_DOWN:
                        player.shoot_2()

                    if event.key == pygame.K_RIGHT:
                        player.shoot_3()

                    if event.key == pygame.K_LEFT:
                        player.shoot_4()                
                  
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        player.speedx += 10

                    if event.key == pygame.K_d:
                        player.speedx -= 10

                    if event.key == pygame.K_w:
                        player.speedy += 10

                    if event.key == pygame.K_s:
                        player.speedy -= 10
        # ----- Atualiza estado do jogo
        # Atualizando a posição dos zombies
        all_sprites.update()
        
        if state == PLAYING:                        
            # Verifica se houve colisão entre os tiros e zombie
            hits = pygame.sprite.groupcollide(all_zombies, all_bullets_1, True, True, pygame.sprite.collide_mask)
            for zombie_1 in hits: # As chaves são os elementos do primeiro grupo (zombies) que colidiram com alguma bala
                # O zombie e destruido
                # No lugar do zombie antigo, adicionar sangue.
                sangue_1 = Sangue(zombie_1.rect.center, dic_recursos)
                all_sprites.add(sangue_1)
                
            hits = pygame.sprite.groupcollide(all_zombies, all_bullets_2, True, True, pygame.sprite.collide_mask)
            for zombie_1 in hits: # As chaves são os elementos do primeiro grupo (zombies) que colidiram com alguma bala
                # O zombie e destruido
                # No lugar do zombie antigo, adicionar sangue.
                sangue_1 = Sangue(zombie_1.rect.center, dic_recursos)
                all_sprites.add(sangue_1)
        
            hits = pygame.sprite.groupcollide(all_zombies, all_bullets_2, True, True, pygame.sprite.collide_mask)
            for zombie_2 in hits: # As chaves são os elementos do primeiro grupo (zombies) que colidiram com alguma bala
                # O zombie e destruido
                # No lugar do zombie antigo, adicionar sangue.
                sangue_2 = Sangue(zombie_2.rect.center, dic_recursos)
                all_sprites.add(sangue_2)

            hits = pygame.sprite.groupcollide(all_zombies, all_bullets_3, True, True, pygame.sprite.collide_mask)
            for zombie_3 in hits: # As chaves são os elementos do primeiro grupo (zombies) que colidiram com alguma bala
                # O zombie e destruido
                # No lugar do zombie antigo, adicionar sangue.
                sangue_3 = Sangue(zombie_3.rect.center, dic_recursos)
                all_sprites.add(sangue_3)

            hits = pygame.sprite.groupcollide(all_zombies, all_bullets_4, True, True, pygame.sprite.collide_mask)
            for zombie_4 in hits: # As chaves são os elementos do primeiro grupo (zombies) que colidiram com alguma bala
                # O zombie e destruido
                # No lugar do zombie antigo, adicionar sangue.
                sangue_4 = Sangue(zombie_4.rect.center, dic_recursos)
                all_sprites.add(sangue_4)

            # Verifica se houve colisão entre player e zombie
            hits = pygame.sprite.spritecollide(player, all_zombies, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                player.kill()
                state = DONE
                
            # Se os zombies acabarem o jogo ficha
            if len(all_zombies) == 0:
                state = DONE
        # ----- Gera saídas
        window.fill((0, 0, 0))  # Preenche com a cor branca
        window.blit(dic_recursos['fundo'], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

        pygame.display.update()  # Mostra o novo frame para o jogador

game_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


