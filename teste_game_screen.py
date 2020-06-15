# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 17:28:41 2020

@author: pedro
"""

import pygame
from teste_config import FPS, WIDTH, HEIGHT, BLACK
from teste_load_dic_recursos import load_dic_recursos, FUNDO, AMMO
from teste_sprites import Zombie, Sobrevivente, Sangue, Caixa

def game_screen(window, morto):
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
    caixa = Caixa(dic_recursos)
    all_sprites.add(player)
    all_sprites.add(caixa)
    
    # Criando os zombies
    for i in range(8):
        zombie = Zombie(dic_recursos)
        all_sprites.add(zombie)
        all_zombies.add(zombie)

    DONE = 0
    PLAYING = 1
    state = PLAYING
    
    MUNICAO = 20
    
    morto = False
    
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
                
                    if MUNICAO > 0:
                        
                        if event.key == pygame.K_UP:
                            MUNICAO = MUNICAO - 1
                            player.shoot_1()
                    
                        if event.key == pygame.K_DOWN:
                            MUNICAO = MUNICAO - 1
                            player.shoot_2()

                        if event.key == pygame.K_RIGHT:
                            MUNICAO = MUNICAO - 1
                            player.shoot_3()

                        if event.key == pygame.K_LEFT:
                            MUNICAO = MUNICAO - 1
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
                morto = True
                return morto
            # Se os zombies acabarem o jogo ficha
            if len(all_zombies) == 0:
                state = DONE
        # ----- Gera saídas
        window.fill((BLACK))  # Preenche com a cor branca
        window.blit(dic_recursos[FUNDO], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)
        
        text_surface = dic_recursos[AMMO].render("munição:{:0}".format(MUNICAO), True, (255, 255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH - 170,  20)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
