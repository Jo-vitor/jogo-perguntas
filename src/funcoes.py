import pygame
from src.config import (
    CORES   
)

cores_rentangulos = [
    CORES["BRANCO"],
    CORES["BRANCO"],
    CORES["BRANCO"],
    CORES["BRANCO"]
]

def criar_resposta():
    respostas = []

    top = 300
    for i in range(4):
        resposta = pygame.Rect(250, top, 300, 50)
        respostas.append(resposta)
        top += 70

    return respostas

def desenhar_inico_jogo(tela, respostas):
    pergunta = pygame.Rect(200, 50, 400, 200)

    tela.fill(CORES["CINZA"])
        
    pygame.draw.rect(tela, CORES["BRANCO"], pergunta, 0, 20)

    for i in range(4):
        pygame.draw.rect(tela, cores_rentangulos[i], respostas[i], 0, 10)

def selecionar_resposta(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_1:
            cores_rentangulos[0] = CORES["VERDE"]
        else:
            cores_rentangulos[0] = CORES["BRANCO"]

        if evento.key == pygame.K_2:
            cores_rentangulos[1] = CORES["VERDE"]
        else:
            cores_rentangulos[1] = CORES["BRANCO"]

        if evento.key == pygame.K_3:
            cores_rentangulos[2] = CORES["VERDE"]
        else:
            cores_rentangulos[2] = CORES["BRANCO"]

        if evento.key == pygame.K_4:
            cores_rentangulos[3] = CORES["VERDE"]
        else:
            cores_rentangulos[3] = CORES["BRANCO"]