# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 02:26:47 2020

@author: pedro
"""

import random
import pygame
from teste_config import WIDTH, HEIGHT, ZOMBIE_WIDTH, ZOMBIE_HEIGHT
from teste_load_dic_recursos import ZOMBIE_IMG, SOBREVIVENTE_IMG, TIRO_1, TIRO_2, TIRO_3, TIRO_4, SANGUE_ANIM

# Criando as classes

#       Zombies
class Zombie(pygame.sprite.Sprite):
    def __init__(self, dic_recursos):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = dic_recursos[ZOMBIE_IMG]
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

        self.image = dic_recursos[TIRO_1]
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

        self.image = dic_recursos[TIRO_2]
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

        self.image = dic_recursos[TIRO_3]
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

        self.image = dic_recursos[TIRO_4]
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

        self.image = dic_recursos[SOBREVIVENTE_IMG]
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
        self.sangue_anim = dic_recursos[SANGUE_ANIM]

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