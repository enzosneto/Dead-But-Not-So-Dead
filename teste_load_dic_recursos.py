# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:29:41 2020

@author: pedro
"""

import pygame
import os
from teste_config import WIDTH, HEIGHT, ZOMBIE_WIDTH, ZOMBIE_HEIGHT, SURVIVOR_WIDTH, SURVIVOR_HEIGHT, BALA_WIDTH, BALA_HEIGTH, CAIXA_WIDTH, CAIXA_HEIGTH, IMG_DIR

# Cria os recursos do minigame

FUNDO = 'fundo'
FUNDO = 'fundo'
ZOMBIE_IMG = 'zombie_img'
ZOMBIE_IMG = 'zombie_img'
SOBREVIVENTE_IMG = 'sobrevivente_img'
SOBREVIVENTE_IMG = 'sobrevivente_img'
TIRO_1 = 'tiro_1'
TIRO_1 = 'tiro_1'
TIRO_2 = 'tiro_2'
TIRO_2 = 'tiro_2'
TIRO_3 = 'tiro_3'
TIRO_3 = 'tiro_3'
TIRO_4 = 'tiro_4'
TIRO_4 = 'tiro_4'
SANGUE_ANIM = 'sangue_anim'
CAIXA = 'caixa'
AMMO =  'ammo'

def load_dic_recursos():
    dic_recursos = {}

    dic_recursos[FUNDO] = pygame.image.load(os.path.join(IMG_DIR, 'background_prototipo.png')).convert()
    dic_recursos[FUNDO] = pygame.transform.scale(dic_recursos['fundo'], (WIDTH, HEIGHT))
    dic_recursos[ZOMBIE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'zombie_prototipo.png')).convert_alpha()
    dic_recursos[ZOMBIE_IMG] = pygame.transform.scale(dic_recursos['zombie_img'], (ZOMBIE_WIDTH, ZOMBIE_HEIGHT))
    dic_recursos[SOBREVIVENTE_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'Player_test1.png')).convert_alpha()
    dic_recursos[SOBREVIVENTE_IMG] = pygame.transform.scale(dic_recursos['sobrevivente_img'], (SURVIVOR_WIDTH, SURVIVOR_HEIGHT))
    dic_recursos[TIRO_1] = pygame.image.load(os.path.join(IMG_DIR, 'tiro_cima.png')).convert_alpha()
    dic_recursos[TIRO_1] = pygame.transform.scale(dic_recursos['tiro_1'], (BALA_WIDTH, BALA_HEIGTH))

    dic_recursos[TIRO_2] = pygame.image.load(os.path.join(IMG_DIR, 'tiro_baixo.png')).convert_alpha()
    dic_recursos[TIRO_2] = pygame.transform.scale(dic_recursos['tiro_2'], (BALA_WIDTH, BALA_HEIGTH))

    dic_recursos[TIRO_3] = pygame.image.load(os.path.join(IMG_DIR, 'tiro_direita.png')).convert_alpha()
    dic_recursos[TIRO_3] = pygame.transform.scale(dic_recursos['tiro_3'], (BALA_WIDTH, BALA_HEIGTH))

    dic_recursos[TIRO_4] = pygame.image.load(os.path.join(IMG_DIR, 'tiro_esquerda.png')).convert_alpha()
    dic_recursos[TIRO_4] = pygame.transform.scale(dic_recursos['tiro_4'], (BALA_WIDTH, BALA_HEIGTH))
    
    dic_recursos[CAIXA] = pygame.image.load(os.path.join(IMG_DIR, 'caixa.png')).convert()
    dic_recursos[CAIXA] = pygame.transform.scale(dic_recursos['caixa'], (CAIXA_WIDTH, CAIXA_HEIGTH))
    dic_recursos[AMMO] = pygame.font.Font('fontes/ammo_font.ttf', 28)
    
    # Animação da morte

    sangue_anim = []
    for i in range(4):
        arquivo = os.path.join(IMG_DIR, 'sangue_img0{}.png'.format(i))
        anim = pygame.image.load(arquivo).convert()
        anim = pygame.transform.scale(anim, (40, 40))
        sangue_anim.append(anim)
    dic_recursos[SANGUE_ANIM] = sangue_anim
    
    return dic_recursos
