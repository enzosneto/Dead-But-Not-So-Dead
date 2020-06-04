# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 02:29:07 2020

@author: pedro
"""

from os import path

# Estabelece a pasta que contem as figuras e sons.
IMG_DIR = path.join(path.dirname(__file__), 'img')

# Dados gerais do jogo.
WIDTH = 800 # Largura da tela
HEIGHT = 800 # Altura da tela
FPS = 30# Frames por segundo

# Define tamanhos
ZOMBIE_WIDTH = 120
ZOMBIE_HEIGHT = 100
SURVIVOR_WIDTH = 50
SURVIVOR_HEIGHT = 38
BALA_WIDTH = 15
BALA_HEIGTH = 20

# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Estados para controle do fluxo da aplicação
INIT = 0
GAME = 1
QUIT = 2
