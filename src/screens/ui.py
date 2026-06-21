import pygame

from src.config import (
    ALTURA_TELA,
    LARGURA_TELA,
    TITULO_JOGO,
)

FUNDO = (18, 24, 38)
FUNDO_SECUNDARIO = (26, 34, 52)
CARTAO = (242, 245, 250)
CARTAO_ESCURO = (34, 45, 67)
BRANCO = (255, 255, 255)
PRETO = (18, 24, 38)
CINZA = (220, 226, 235)
CINZA_TEXTO = (115, 124, 140)
VERDE = (46, 204, 113)
VERDE_ESCURO = (34, 166, 91)
VERMELHO = (231, 76, 60)
AZUL = (52, 152, 219)
AMARELO = (241, 196, 15)


def desenhar_texto(tela, texto, fonte, cor, x, y, center=False):
    superficie = fonte.render(str(texto), True, cor)
    rect = superficie.get_rect()

    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)

    tela.blit(superficie, rect)
    return rect


def quebrar_texto(texto, fonte, largura_maxima):
    palavras = str(texto).split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = palavra if linha_atual == "" else linha_atual + " " + palavra

        if fonte.size(teste)[0] <= largura_maxima:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas


def desenhar_texto_quebrado(tela, texto, fonte, cor, x, y, largura_maxima, espaco=8, center=False):
    linhas = quebrar_texto(texto, fonte, largura_maxima)
    altura_linha = fonte.get_height() + espaco

    for indice, linha in enumerate(linhas):
        pos_y = y + indice * altura_linha

        if center:
            desenhar_texto(tela, linha, fonte, cor, x, pos_y, center=True)
        else:
            desenhar_texto(tela, linha, fonte, cor, x, pos_y)

    return len(linhas) * altura_linha


def desenhar_painel(tela, retangulo, cor, borda=None, raio=18):
    pygame.draw.rect(tela, cor, retangulo, border_radius=raio)

    if borda:
        pygame.draw.rect(tela, borda, retangulo, 2, border_radius=raio)


def desenhar_botao(tela, retangulo, texto, fonte, selecionado=False, cor_base=None):
    if cor_base is None:
        cor_base = VERDE if selecionado else CARTAO

    cor_borda = VERDE if selecionado else CINZA
    cor_texto = BRANCO if selecionado else PRETO

    desenhar_painel(tela, retangulo, cor_base, cor_borda, 16)
    desenhar_texto(tela, texto, fonte, cor_texto, retangulo.centerx, retangulo.centery, center=True)


def criar_retangulos_opcoes():
    largura_retangulo = 660
    altura_retangulo = 68
    espacamento = 14
    pos_x = 70
    pos_y = 285
    retangulos = []

    for i in range(4):
        retangulos.append(
            pygame.Rect(
                pos_x,
                pos_y + i * (altura_retangulo + espacamento),
                largura_retangulo,
                altura_retangulo,
            )
        )

    return retangulos


def desenhar_tela_menu(tela, fonte_titulo, fonte_menu, opcoes, selecionado, status_api):
    tela.fill(FUNDO)

    painel = pygame.Rect(80, 60, 640, 480)
    desenhar_painel(tela, painel, CARTAO, None, 26)

    desenhar_texto(tela, TITULO_JOGO, fonte_titulo, PRETO, 400, 120, center=True)
    desenhar_texto(
        tela,
        "Quiz de esportes com perguntas, tempo, pontuação e ranking local",
        fonte_menu,
        CINZA_TEXTO,
        400,
        165,
        center=True,
    )

    for indice, opcao in enumerate(opcoes):
        retangulo = pygame.Rect(250, 230 + indice * 82, 300, 58)
        desenhar_botao(tela, retangulo, opcao, fonte_menu, selecionado=(indice == selecionado))

    status_limpo = str(status_api)
    if len(status_limpo) > 55:
        status_limpo = status_limpo[:55] + "..."

    desenhar_texto(
        tela,
        status_limpo,
        fonte_menu,
        CINZA_TEXTO,
        400,
        500,
        center=True,
    )

    desenhar_texto(
        tela,
        "Use W/S ou as setas para navegar. ENTER seleciona.",
        fonte_menu,
        BRANCO,
        400,
        570,
        center=True,
    )


def desenhar_tela_status(tela, fonte_texto, pontos, recorde, indice_pergunta, total_perguntas, tempo_restante):
    barra = pygame.Rect(0, 0, LARGURA_TELA, 82)
    pygame.draw.rect(tela, FUNDO, barra)

    desenhar_texto(tela, TITULO_JOGO, fonte_texto, BRANCO, 32, 28)

    desenhar_texto(
        tela,
        f"Pergunta {indice_pergunta + 1}/{total_perguntas}",
        fonte_texto,
        BRANCO,
        250,
        28,
    )

    desenhar_texto(
        tela,
        f"Pontos: {pontos}",
        fonte_texto,
        VERDE,
        455,
        28,
    )

    desenhar_texto(
        tela,
        f"Recorde: {recorde}",
        fonte_texto,
        AMARELO,
        585,
        28,
    )

    cor_tempo = VERMELHO if tempo_restante <= 5 else BRANCO
    desenhar_texto(
        tela,
        f"Tempo: {tempo_restante}s",
        fonte_texto,
        cor_tempo,
        32,
        92,
    )


def desenhar_tela_ranking(tela, fonte_titulo, fonte_menu, ranking):
    tela.fill(FUNDO)

    painel = pygame.Rect(90, 55, 620, 490)
    desenhar_painel(tela, painel, CARTAO, None, 24)

    desenhar_texto(tela, "Ranking", fonte_titulo, PRETO, 400, 105, center=True)
    desenhar_texto(tela, "Melhores pontuações salvas no computador", fonte_menu, CINZA_TEXTO, 400, 150, center=True)

    if not ranking:
        desenhar_texto(
            tela,
            "Ainda não há pontuações salvas.",
            fonte_menu,
            PRETO,
            400,
            280,
            center=True,
        )
    else:
        for indice, pontuacao in enumerate(ranking[:10], start=1):
            y = 190 + 32 * indice
            texto = f"{indice}. {pontuacao} pontos"
            cor = VERDE_ESCURO if indice == 1 else PRETO
            desenhar_texto(tela, texto, fonte_menu, cor, 400, y, center=True)

    desenhar_texto(
        tela,
        "Pressione ESC para voltar ao menu.",
        fonte_menu,
        BRANCO,
        400,
        570,
        center=True,
    )


def desenhar_tela_pergunta(
    tela,
    pergunta,
    fonte_texto,
    fonte_menu,
    opcoes_retangulos,
    selecionado,
    estado_feedback,
    texto_feedback,
    cor_feedback,
):
    painel_pergunta = pygame.Rect(50, 135, 700, 120)
    desenhar_painel(tela, painel_pergunta, CARTAO, None, 18)

    desenhar_texto_quebrado(
        tela,
        pergunta["pergunta"],
        fonte_texto,
        PRETO,
        400,
        170,
        620,
        espaco=6,
        center=True,
    )

    for indice, opcao in enumerate(pergunta["opcoes"]):
        retangulo = opcoes_retangulos[indice]

        cor_retangulo = CARTAO
        cor_borda = CINZA
        cor_texto = PRETO

        if estado_feedback:
            if indice == pergunta["resposta"]:
                cor_retangulo = VERDE
                cor_borda = VERDE_ESCURO
                cor_texto = BRANCO
            elif selecionado == indice:
                cor_retangulo = VERMELHO
                cor_borda = VERMELHO
                cor_texto = BRANCO
        elif selecionado == indice:
            cor_retangulo = AZUL
            cor_borda = AZUL
            cor_texto = BRANCO

        desenhar_painel(tela, retangulo, cor_retangulo, cor_borda, 16)

        desenhar_texto_quebrado(
            tela,
            f"{indice + 1}. {opcao}",
            fonte_menu,
            cor_texto,
            retangulo.x + 22,
            retangulo.y + 18,
            retangulo.width - 44,
            espaco=3,
            center=False,
        )

    faixa = pygame.Rect(50, 548, 700, 36)

    if estado_feedback:
        desenhar_painel(tela, faixa, CARTAO, None, 12)
        desenhar_texto(tela, texto_feedback, fonte_menu, cor_feedback, 400, 566, center=True)
    else:
        desenhar_texto(
            tela,
            "Responda usando 1, 2, 3, 4 ou clique na alternativa.",
            fonte_menu,
            FUNDO,
            400,
            565,
            center=True,
        )


def desenhar_tela_final(tela, fonte_titulo, fonte_texto, fonte_menu, pontos, recorde):
    tela.fill(FUNDO)

    painel = pygame.Rect(90, 70, 620, 430)
    desenhar_painel(tela, painel, CARTAO, None, 24)

    desenhar_texto(tela, "Fim de jogo", fonte_titulo, PRETO, 400, 130, center=True)

    desenhar_texto(
        tela,
        f"Pontuação final: {pontos}",
        fonte_texto,
        PRETO,
        400,
        220,
        center=True,
    )

    desenhar_texto(
        tela,
        f"Recorde atual: {recorde}",
        fonte_texto,
        VERDE_ESCURO,
        400,
        270,
        center=True,
    )

    if pontos >= recorde and pontos > 0:
        mensagem = "Excelente! Você igualou ou superou o recorde."
    elif pontos > 0:
        mensagem = "Boa partida! Tente novamente para subir no ranking."
    else:
        mensagem = "Tente novamente para melhorar sua pontuação."

    desenhar_texto_quebrado(
        tela,
        mensagem,
        fonte_menu,
        CINZA_TEXTO,
        400,
        335,
        520,
        center=True,
    )

    desenhar_texto(
        tela,
        "Pressione ENTER para voltar ao menu ou ESC para sair.",
        fonte_menu,
        BRANCO,
        400,
        570,
        center=True,
    )