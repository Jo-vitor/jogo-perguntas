import os
import random
import pygame

from src.config import (
    ALTURA_TELA,
    AZUL,
    BRANCO,
    CAMINHO_PERGUNTAS,
    CAMINHO_RANKING,
    CAMINHO_RECORDE,
    FPS,
    LARGURA_TELA,
    NUM_PERGUNTAS,
    PONTOS_CORRETO,
    TEMPO_POR_PERGUNTA,
    VERDE,
    VERMELHO,
)
from src.funcoes import calcular_pontos, verificar_resposta
from src.services.data_service import (
    adicionar_ranking,
    carregar_perguntas_locais,
    carregar_ranking,
    carregar_recorde,
    salvar_recorde,
)

from src.screens.ui import (
    criar_retangulos_opcoes,
    desenhar_tela_final,
    desenhar_tela_menu,
    desenhar_tela_pergunta,
    desenhar_tela_ranking,
    desenhar_tela_status,
)


def carregar_perguntas():
    origem = "Perguntas carregadas do arquivo local"
    perguntas = carregar_perguntas_locais(CAMINHO_PERGUNTAS)

    if not perguntas:
        perguntas = [
            {
                "pergunta": "O banco de perguntas não foi encontrado.",
                "opcoes": [
                    "Verifique o arquivo data/perguntas.json",
                    "Confira se o projeto está na pasta correta",
                    "Reinicie o jogo",
                    "Volte ao menu principal",
                ],
                "resposta": 0,
            }
        ]
        origem = "Banco local não encontrado"

    if len(perguntas) > NUM_PERGUNTAS:
        perguntas = random.sample(perguntas, NUM_PERGUNTAS)

    return perguntas, origem


def executar_jogo():
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption("SportQuiz")

    relogio = pygame.time.Clock()
    fonte_titulo = pygame.font.SysFont(None, 52)
    fonte_texto = pygame.font.SysFont(None, 28)
    fonte_menu = pygame.font.SysFont(None, 24)

    menu_opcoes = ["Iniciar partida", "Ranking", "Sair"]
    menu_selecionado = 0
    estado = "menu"
    status_api = "Carregando perguntas..."
    perguntas, status_api = carregar_perguntas()
    recorde = carregar_recorde(CAMINHO_RECORDE)
    ranking = carregar_ranking(CAMINHO_RANKING)

    indice_pergunta = 0
    pontos = 0
    tempo_restante = TEMPO_POR_PERGUNTA
    estado_feedback = False
    texto_feedback = ""
    cor_feedback = AZUL
    feedback_timer = 0.0
    selecionado = None
    opcoes_retangulos = criar_retangulos_opcoes()
    opcao_por_tecla = {
        pygame.K_1: 0,
        pygame.K_2: 1,
        pygame.K_3: 2,
        pygame.K_4: 3,
        pygame.K_KP1: 0,
        pygame.K_KP2: 1,
        pygame.K_KP3: 2,
        pygame.K_KP4: 3,
    }

    def iniciar_partida():
        nonlocal perguntas, status_api, indice_pergunta, pontos, tempo_restante, estado_feedback
        nonlocal texto_feedback, cor_feedback, feedback_timer, selecionado, estado, recorde, ranking

        perguntas, status_api = carregar_perguntas()
        indice_pergunta = 0
        pontos = 0
        tempo_restante = TEMPO_POR_PERGUNTA
        estado_feedback = False
        texto_feedback = ""
        cor_feedback = AZUL
        feedback_timer = 0.0
        selecionado = None
        estado = "playing"
        recorde = carregar_recorde(CAMINHO_RECORDE)
        ranking = carregar_ranking(CAMINHO_RANKING)

    while True:
        delta = relogio.tick(FPS) / 1000.0

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return

            if evento.type == pygame.KEYDOWN:
                if estado == "menu":
                    if evento.key in (pygame.K_UP, pygame.K_w):
                        menu_selecionado = (menu_selecionado - 1) % len(menu_opcoes)
                    elif evento.key in (pygame.K_DOWN, pygame.K_s):
                        menu_selecionado = (menu_selecionado + 1) % len(menu_opcoes)
                    elif evento.key == pygame.K_RETURN:
                        if menu_selecionado == 0:
                            iniciar_partida()
                        elif menu_selecionado == 1:
                            ranking = carregar_ranking(CAMINHO_RANKING)
                            estado = "ranking"
                        elif menu_selecionado == 2:
                            pygame.quit()
                            return

                elif estado == "playing":
                    if evento.key == pygame.K_ESCAPE:
                        estado = "menu"
                    elif evento.key in opcao_por_tecla and not estado_feedback:
                        selecionado = opcao_por_tecla[evento.key]

                elif estado in ("results", "ranking"):
                    if evento.key == pygame.K_ESCAPE:
                        if estado == "results":
                            pygame.quit()
                            return
                        estado = "menu"
                    elif evento.key == pygame.K_RETURN and estado == "results":
                        estado = "menu"

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if estado == "playing" and not estado_feedback:
                    for indice, retangulo in enumerate(opcoes_retangulos):
                        if retangulo.collidepoint(evento.pos):
                            selecionado = indice
                            break

        if estado == "playing":
            if indice_pergunta < len(perguntas) and not estado_feedback:
                tempo_restante -= delta
                if tempo_restante <= 0:
                    resposta_correta = perguntas[indice_pergunta]["resposta"]
                    texto_feedback = (
                        f"Tempo esgotado! Resposta certa: {perguntas[indice_pergunta]['opcoes'][resposta_correta]}"
                    )
                    cor_feedback = VERMELHO
                    estado_feedback = True
                    feedback_timer = 1.2

            if selecionado is not None and indice_pergunta < len(perguntas) and not estado_feedback:
                resposta_correta = perguntas[indice_pergunta]["resposta"]
                if verificar_resposta(selecionado, resposta_correta):
                    pontos = calcular_pontos(pontos, PONTOS_CORRETO)
                    texto_feedback = "Resposta correta! +100 pontos"
                    cor_feedback = VERDE
                else:
                    texto_feedback = (
                        f"Errado! Resposta certa: {perguntas[indice_pergunta]['opcoes'][resposta_correta]}"
                    )
                    cor_feedback = VERMELHO
                estado_feedback = True
                feedback_timer = 1.2

            if estado_feedback:
                feedback_timer -= delta
                if feedback_timer <= 0:
                    selecionado = None
                    estado_feedback = False
                    indice_pergunta += 1
                    tempo_restante = TEMPO_POR_PERGUNTA

                    if indice_pergunta >= len(perguntas):
                        recorde = max(recorde, pontos)
                        salvar_recorde(CAMINHO_RECORDE, recorde)
                        ranking = adicionar_ranking(CAMINHO_RANKING, pontos)
                        estado = "results"

        tela.fill(BRANCO)

        if estado == "menu":
            desenhar_tela_menu(tela, fonte_titulo, fonte_menu, menu_opcoes, menu_selecionado, status_api)
        elif estado == "ranking":
            desenhar_tela_ranking(tela, fonte_titulo, fonte_menu, ranking)
        elif estado == "playing":
            pergunta = perguntas[indice_pergunta]
            desenhar_tela_status(
                tela,
                fonte_texto,
                pontos,
                recorde,
                indice_pergunta,
                len(perguntas),
                int(tempo_restante),
            )
            desenhar_tela_pergunta(
                tela,
                pergunta,
                fonte_texto,
                fonte_menu,
                opcoes_retangulos,
                selecionado,
                estado_feedback,
                texto_feedback,
                cor_feedback,
            )
        else:
            desenhar_tela_final(tela, fonte_titulo, fonte_texto, fonte_menu, pontos, recorde)

        pygame.display.flip()
