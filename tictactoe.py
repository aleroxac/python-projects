#!/usr/bin/env python3


import pygame
from pygame.locals import *
from  time import sleep
from sys import exit

def inicia_tabuleiro():
    global tabuleiro, tela, fundo, simbolo
    simbolo = 'X'

    # Desenhando a janela
    pygame.init()

    tabuleiro = [ [None,None,None], \
                [None,None,None], \
                [None,None,None] ]

    tela = pygame.display.set_mode( (300,300) )
    pygame.display.set_caption('Tic-Tac-Toe')

    ## Setando uma cor de fundo
    fundo = pygame.Surface((300,300))
    fundo.fill((0,0,0))

    ## Desenhando as linhas herticais
    pygame.draw.line(fundo, (150,150,150), (100,0), (100,300), 10)
    pygame.draw.line(fundo, (150,150,150), (200,0), (200,300), 10)
    ## Desenhando as linhas horizontais
    pygame.draw.line(fundo, (150,150,150), (0,100), (300,100), 10)
    pygame.draw.line(fundo, (150,150,150), (0,200), (300,200), 10)



def posicao_tabuleiro():
    linha, coluna = 0, 0

    if pygame.mouse.get_pos()[0] <= 100:
        coluna = 0
    elif pygame.mouse.get_pos()[0] <= 200:
        coluna = 1
    else:
        coluna = 2

    if pygame.mouse.get_pos()[1] <= 100:
        linha = 0
    elif pygame.mouse.get_pos()[1] <= 200:
        linha = 1
    else:
        linha = 2
    return (linha, coluna)




def desenha_movimento(fundo, linha, coluna, simbolo):
    tabuleiro[linha][coluna] = simbolo

    centro_x = (coluna * 100) + 50
    centro_y = (linha * 100) + 50

    if (simbolo == 'O'):
        pygame.draw.circle(fundo, (150,150,150), (centro_x, centro_y), 35, 10)
    else:
        pygame.draw.line(fundo, (150,150,150), (centro_x - 23, centro_y - 23), (centro_x + 23, centro_y + 23), 10)
        pygame.draw.line(fundo, (150,150,150), (centro_x + 23, centro_y - 23), (centro_x - 23, centro_y + 23), 10)


def registra_clique(fundo):
    global tabuleiro, simbolo
    posicao_tabuleiro()
    (linha, coluna) = posicao_tabuleiro()

    if(tabuleiro[linha][coluna] is not None):
        return

    desenha_movimento(fundo, linha, coluna, simbolo)

    if (simbolo == 'X'):
        simbolo = 'O'
    else:
        simbolo = 'X'
    verifica_fim()



def verifica_fim():
    fim = ''

    # Horizontal ----------------------------------------------------- OK
    for simb in ('X','O'):
        if tabuleiro[0] == [simb, simb, simb]:
            pygame.draw.line(fundo, (150,0,0), (0,50), (300,50), 5)
            fim = 'linha1'
        elif tabuleiro[1] == [simb, simb, simb]:
            pygame.draw.line(fundo, (150,0,0), (0,150), (300,150), 5)
            fim = 'linha2'
        elif tabuleiro[2] == [simb, simb, simb]:
            pygame.draw.line(fundo, (150,0,0), (0,250), (300,250), 5)
            fim = 'linha3'


    # Vertical ----------------------------------------------------- OK
    for simb in ('X','O'):
        if simb == tabuleiro[0][0] and simb == tabuleiro[1][0] and simb == tabuleiro[2][0]:
            pygame.draw.line(fundo, (150,0,0), (50,0), (50,300), 5)
            fim = 'coluna1'
        if simb == tabuleiro[0][1] and simb == tabuleiro[1][1] and simb == tabuleiro[2][1]:
            pygame.draw.line(fundo, (150,0,0), (150,0), (150,300), 5)
            fim = 'coluna2'
        elif simb == tabuleiro[0][2] and simb == tabuleiro[1][2] and simb == tabuleiro[2][2]:
            pygame.draw.line(fundo, (150,0,0), (250,0), (250,300), 5)
            fim = 'coluna3'

    # Diagonal ----------------------------------------------------- 
    for simb in ('X','O'):
        if simb == tabuleiro[0][0] and simb == tabuleiro[1][1] and simb == tabuleiro[2][2]:
            pygame.draw.line(fundo, (150,0,0), (0,0), (300,300), 5)
            fim = 'diagonal_esquerda'
        elif simb == tabuleiro[0][2] and simb == tabuleiro[1][1] and simb == tabuleiro[2][0]:
            pygame.draw.line(fundo, (150,0,0), (0,300), (300,0), 5)
            fim = 'diagonal direita'

    if 'linha' in fim or 'coluna' in fim or 'diagonal' in fim:
        print(fim)
        if not 'False' in tabuleiro.items:
            return 1
        return 1


if __name__ == "__main__":
    inicia_tabuleiro()
    rodando = True
    while rodando:
        # Verificando eventos de interação
        for event in pygame.event.get():
            if event.type is QUIT:
                rodando = False
            if event.type is MOUSEBUTTONDOWN:
                registra_clique(fundo)
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                rodando = False
            if verifica_fim() == 1:
                rodando = False


        # Atualizando a tela
        tela.blit(fundo, (0,0))
        pygame.display.flip()

    
