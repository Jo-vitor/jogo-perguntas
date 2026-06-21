import pygame

from src.config import (
    ALTURA_TELA,
    CAMINHO_PERGUNTAS,
    LARGURA_TELA,
    PERGUNTAS_POR_PARTIDA,
    PONTOS_POR_ACERTO,
    TEMPO_FEEDBACK_MS,
    TITULO_JOGO,
    TEMPO_LIMITE
)
from src.funcoes import (
    aplicar_feedback_cores,
    calcular_pontos,
    criar_cores_alternativas,
    criar_fontes,
    criar_rects_resposta,
    desenhar_alternativas,
    desenhar_feedback,
    desenhar_pergunta,
    desenhar_tela_final,
    obter_indice_resposta,
    resetar_cores_alternativas,
    verificar_resposta,
    calcular_tempo
)
from src.perguntas import carregar_perguntas, selecionar_perguntas


def executar_jogo():
    """Executa o loop principal do jogo e controla estado e pontuacao."""
    pygame.init()

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)
    relogio = pygame.time.Clock()

    fontes = criar_fontes()
    rects_resposta = criar_rects_resposta()
    cores_alternativas = criar_cores_alternativas()

    perguntas = selecionar_perguntas(
        carregar_perguntas(CAMINHO_PERGUNTAS),
        PERGUNTAS_POR_PARTIDA,
    )

    indice_pergunta = 0
    pontuacao = 0
    estado = "aguardando"
    indice_selecionado = None
    acertou_ultima = False
    horario_feedback = 0
    inicio = pygame.time.get_ticks()

    rodando = True

    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
                continue

            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                if estado == "fim":
                    rodando = False
                continue

            if estado != "aguardando":
                continue

            indice_resposta = obter_indice_resposta(evento, rects_resposta)
            if indice_resposta is None:
                continue

            pergunta_atual = perguntas[indice_pergunta]
            indice_selecionado = indice_resposta
            acertou_ultima = verificar_resposta(
                indice_selecionado,
                pergunta_atual["correta"],
            )

            if acertou_ultima:
                pontuacao = calcular_pontos(pontuacao, PONTOS_POR_ACERTO)

            aplicar_feedback_cores(
                cores_alternativas,
                indice_selecionado,
                pergunta_atual["correta"],
                acertou_ultima,
            )

            estado = "feedback"
            horario_feedback = pygame.time.get_ticks()

        if estado == "aguardando":
            agora = pygame.time.get_ticks()
            tempo_passado = (agora - inicio) / 1000 
            tempo_restante = TEMPO_LIMITE - tempo_passado
                
            if tempo_restante <= 0:
                acertou_ultima = False
                pergunta_atual = perguntas[indice_pergunta]
                estado = "feedback"
                horario_feedback = pygame.time.get_ticks()
                tempo_restante = 0

        if estado == "feedback":
            tempo_decorrido = pygame.time.get_ticks() - horario_feedback

            if tempo_decorrido >= TEMPO_FEEDBACK_MS:
                indice_pergunta += 1

                if indice_pergunta >= len(perguntas):
                    estado = "fim"
                else:
                    estado = "aguardando"
                    indice_selecionado = None
                    resetar_cores_alternativas(cores_alternativas)
                    inicio = pygame.time.get_ticks()
                    

        if estado == "fim":
            desenhar_tela_final(tela, fontes, pontuacao)
        else:
            pergunta_atual = perguntas[indice_pergunta]
            desenhar_pergunta(
                tela,
                fontes,
                pergunta_atual,
                indice_pergunta,
                len(perguntas),
                pontuacao,
                tempo_restante
            )
            posicao_mouse = pygame.mouse.get_pos()
            indice_hover = None

            if estado == "aguardando":
                for indice, rect in enumerate(rects_resposta):
                    if rect.collidepoint(posicao_mouse):
                        indice_hover = indice
                        break

            desenhar_alternativas(
                tela,
                fontes,
                pergunta_atual["alternativas"],
                rects_resposta,
                cores_alternativas,
                indice_hover=indice_hover,
            )

            if estado == "feedback":
                desenhar_feedback(tela, fontes["feedback"], acertou_ultima, tempo_restante <= 0)

        pygame.display.flip()
        relogio.tick(60)

    pygame.quit()
