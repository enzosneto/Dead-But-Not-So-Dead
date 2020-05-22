# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:31:07 2020

@author: enzos
"""

import os
import pygame
import json
import random

font_name = pygame.font.match_font("arial")

comida = 0
municao = 0
carisma = 0
sobreviventes = 0

atributo_1 = [comida, municao]
atributo_2 = [carisma]

RED = (255,0,0)
YELLOW = (255,255,0)
WHITE = (0,0,0)
BLACK = (255,255,255)

def draw_text(surf, text, size, x, y, frequency, duration, cor):

    for letras in text:
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(letras, True, cor)
        text_rect = text_surface.get_rect()
        text_rect.midtop =  (x,y)
        surf.blit(text_surface, text_rect)
        x = x + 8
        y = y
        
def draw_number(surf, number, size, x, y, frequency, duration, cor):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(str(number), True, cor)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surface, text_rect)