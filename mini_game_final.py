# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:26:20 2020

@author: pedro
"""

# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from teste_config import WIDTH, HEIGHT
from teste_game_screen import game_screen


pygame.init()
pygame.mixer.init()
morto = False
# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mini_game')

game_screen(window,morto)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados
