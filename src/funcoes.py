import pygame

from src.config import (
    ALTURA_BOTAO_ALTERNATIVA,
    ALTURA_CARD_PERGUNTA,
    ALTURA_TELA,
    CORES,
    ESPACO_ENTRE_BOTOES,
    FONTE_NOME,
    FONTE_NOME_FALLBACK,
    FONTE_TAMANHO_ALTERNATIVA,
    FONTE_TAMANHO_FEEDBACK,
    FONTE_TAMANHO_FINAL,
    FONTE_TAMANHO_INFO,
    FONTE_TAMANHO_LABEL,
    FONTE_TAMANHO_PERGUNTA,
    FONTE_TAMANHO_TITULO,
    LARGURA_BADGE,
    LARGURA_CONTEUDO,
    LARGURA_TELA,
    MARGEM,
    PONTOS_POR_ACERTO,
    RAIO_BOTAO,
    RAIO_CARD,
    TITULO_JOGO,
    Y_BARRA_PROGRESSO,
    Y_CARD_PERGUNTA,
    Y_HEADER,
    Y_PRIMEIRA_ALTERNATIVA,
)

LETRAS_ALTERNATIVAS = ("A", "B", "C", "D")
TECLAS_RESPOSTA = {
    pygame.K_1: 0,
    pygame.K_2: 1,
    pygame.K_3: 2,
    pygame.K_4: 3,
}


def calcular_pontos(pontuacao_atual, pontos_ganhos):
    """Soma os pontos ganhos a pontuacao atual."""
    return pontuacao_atual + pontos_ganhos


def verificar_resposta(indice_selecionado, indice_correto):
    """Retorna True quando a alternativa selecionada e a correta."""
    return indice_selecionado == indice_correto


def _criar_fonte(tamanho, negrito=False):
    """Cria fonte do sistema com fallback."""
    for nome in (FONTE_NOME, FONTE_NOME_FALLBACK, None):
        try:
            return pygame.font.SysFont(nome, tamanho, bold=negrito)
        except Exception:
            continue

    return pygame.font.Font(None, tamanho)


def criar_fontes():
    """Cria as fontes usadas nas telas do jogo."""
    return {
        "titulo": _criar_fonte(FONTE_TAMANHO_TITULO, negrito=True),
        "pergunta": _criar_fonte(FONTE_TAMANHO_PERGUNTA),
        "alternativa": _criar_fonte(FONTE_TAMANHO_ALTERNATIVA),
        "info": _criar_fonte(FONTE_TAMANHO_INFO),
        "label": _criar_fonte(FONTE_TAMANHO_LABEL, negrito=True),
        "feedback": _criar_fonte(FONTE_TAMANHO_FEEDBACK, negrito=True),
        "final": _criar_fonte(FONTE_TAMANHO_FINAL, negrito=True),
    }


def criar_rects_resposta():
    """Cria os retangulos clicaveis das quatro alternativas."""
    rects = []
    topo = Y_PRIMEIRA_ALTERNATIVA

    for _ in range(4):
        rects.append(pygame.Rect(MARGEM, topo, LARGURA_CONTEUDO, ALTURA_BOTAO_ALTERNATIVA))
        topo += ALTURA_BOTAO_ALTERNATIVA + ESPACO_ENTRE_BOTOES

    return rects


def criar_cores_alternativas():
    """Inicializa as cores das alternativas."""
    return [CORES["CARD"]] * 4


def resetar_cores_alternativas(cores):
    """Restaura todas as alternativas para a cor padrao."""
    for indice in range(len(cores)):
        cores[indice] = CORES["CARD"]


def aplicar_feedback_cores(cores, indice_selecionado, indice_correto, acertou):
    """Define as cores das alternativas apos a resposta do jogador."""
    resetar_cores_alternativas(cores)

    if acertou:
        cores[indice_selecionado] = CORES["VERDE_FUNDO"]
        return

    cores[indice_selecionado] = CORES["VERMELHO_FUNDO"]
    cores[indice_correto] = CORES["VERDE_FUNDO"]


def obter_indice_resposta(evento, rects):
    """Retorna o indice da alternativa escolhida ou None."""
    if evento.type == pygame.KEYDOWN and evento.key in TECLAS_RESPOSTA:
        return TECLAS_RESPOSTA[evento.key]

    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
        posicao = evento.pos

        for indice, rect in enumerate(rects):
            if rect.collidepoint(posicao):
                return indice

    return None


def _desenhar_fundo(tela):
    """Preenche a tela com a cor de fundo principal."""
    tela.fill(CORES["FUNDO"])


def _desenhar_card(tela, rect, cor_fundo, cor_borda=CORES["BORDA"], espessura_borda=2):
    """Desenha um card arredondado com borda."""
    pygame.draw.rect(tela, cor_fundo, rect, border_radius=RAIO_CARD)
    pygame.draw.rect(tela, cor_borda, rect, espessura_borda, border_radius=RAIO_CARD)


def _quebrar_texto(fonte, texto, largura_max):
    """Quebra texto longo em multiplas linhas."""
    palavras = texto.split()
    linhas = []
    linha_atual = ""

    for palavra in palavras:
        teste = f"{linha_atual} {palavra}".strip()

        if fonte.size(teste)[0] <= largura_max:
            linha_atual = teste
        else:
            if linha_atual:
                linhas.append(linha_atual)
            linha_atual = palavra

    if linha_atual:
        linhas.append(linha_atual)

    return linhas or [texto]


def _desenhar_texto_centralizado(tela, fonte, texto, centro_y, cor=CORES["TEXTO"], centro_x=None):
    """Desenha um texto centralizado horizontalmente."""
    superficie = fonte.render(texto, True, cor)
    pos_x = centro_x if centro_x is not None else LARGURA_TELA // 2
    rect = superficie.get_rect(center=(pos_x, centro_y))
    tela.blit(superficie, rect)


def _desenhar_texto_multilinha(tela, fonte, linhas, rect, cor=CORES["TEXTO"], espacamento=8):
    """Desenha varias linhas de texto centralizadas dentro de um retangulo."""
    altura_total = len(linhas) * fonte.get_height() + (len(linhas) - 1) * espacamento
    inicio_y = rect.y + (rect.height - altura_total) // 2

    for indice, linha in enumerate(linhas):
        superficie = fonte.render(linha, True, cor)
        pos_x = rect.x + (rect.width - superficie.get_width()) // 2
        pos_y = inicio_y + indice * (fonte.get_height() + espacamento)
        tela.blit(superficie, (pos_x, pos_y))


def _desenhar_texto_em_rect(tela, fonte, texto, rect, cor=CORES["TEXTO"], margem=12):
    """Desenha texto alinhado a esquerda dentro de um retangulo."""
    superficie = fonte.render(texto, True, cor)
    posicao = (rect.x + margem, rect.y + (rect.height - superficie.get_height()) // 2)
    tela.blit(superficie, posicao)


def _desenhar_barra_progresso(tela, indice, total):
    """Desenha a barra de progresso abaixo do cabecalho."""
    largura_barra = LARGURA_CONTEUDO
    altura_barra = 8
    rect_fundo = pygame.Rect(MARGEM, Y_BARRA_PROGRESSO, largura_barra, altura_barra)
    pygame.draw.rect(tela, CORES["BORDA"], rect_fundo, border_radius=4)

    if total > 0:
        progresso = (indice + 1) / total
        largura_preenchida = int(largura_barra * progresso)
        rect_progresso = pygame.Rect(MARGEM, Y_BARRA_PROGRESSO, largura_preenchida, altura_barra)
        pygame.draw.rect(tela, CORES["DESTAQUE"], rect_progresso, border_radius=4)


def _desenhar_badge(tela, fontes, letra, rect_botao, cor_fundo=CORES["DESTAQUE"]):
    """Desenha o badge com a letra da alternativa."""
    badge_rect = pygame.Rect(
        rect_botao.x + 12,
        rect_botao.centery - LARGURA_BADGE // 2,
        LARGURA_BADGE,
        LARGURA_BADGE,
    )
    pygame.draw.rect(tela, cor_fundo, badge_rect, border_radius=RAIO_BOTAO)
    _desenhar_texto_centralizado(
        tela,
        fontes["alternativa"],
        letra,
        badge_rect.centery,
        CORES["TEXTO_CLARO"],
        badge_rect.centerx,
    )


def _desenhar_header(tela, fontes, indice, total, pontuacao):
    """Desenha o cabecalho com titulo, progresso e pontuacao."""
    _desenhar_texto_em_rect(
        tela,
        fontes["titulo"],
        TITULO_JOGO,
        pygame.Rect(MARGEM, Y_HEADER, 200, 40),
        CORES["TEXTO_CLARO"],
        margem=0,
    )

    _desenhar_texto_centralizado(
        tela,
        fontes["info"],
        f"Pergunta {indice + 1} de {total}",
        Y_HEADER + 20,
        CORES["TEXTO_CLARO"],
    )

    badge_pontos = pygame.Rect(LARGURA_TELA - MARGEM - 110, Y_HEADER + 4, 110, 32)
    _desenhar_card(tela, badge_pontos, CORES["DESTAQUE"], CORES["DESTAQUE"])
    _desenhar_texto_centralizado(
        tela,
        fontes["info"],
        f"{pontuacao} pts",
        badge_pontos.centery,
        CORES["TEXTO_CLARO"],
        badge_pontos.centerx,
    )


def _desenhar_rodape(tela, fontes):
    """Desenha a dica de controles na parte inferior."""
    _desenhar_texto_centralizado(
        tela,
        fontes["info"],
        "Pressione 1-4 ou clique para responder",
        ALTURA_TELA - 25,
        CORES["TEXTO_SECUNDARIO"],
    )


def desenhar_pergunta(tela, fontes, pergunta_atual, indice, total, pontuacao):
    """Desenha o enunciado, progresso e pontuacao atual."""
    _desenhar_fundo(tela)
    _desenhar_header(tela, fontes, indice, total, pontuacao)
    _desenhar_barra_progresso(tela, indice, total)

    pergunta_rect = pygame.Rect(MARGEM, Y_CARD_PERGUNTA, LARGURA_CONTEUDO, ALTURA_CARD_PERGUNTA)
    _desenhar_card(tela, pergunta_rect, CORES["CARD"])

    label_rect = pygame.Rect(pergunta_rect.x + 20, pergunta_rect.y + 14, 120, 20)
    _desenhar_texto_em_rect(
        tela,
        fontes["label"],
        "PERGUNTA",
        label_rect,
        CORES["DESTAQUE"],
        margem=0,
    )

    texto_rect = pygame.Rect(
        pergunta_rect.x + 20,
        pergunta_rect.y + 38,
        pergunta_rect.width - 40,
        pergunta_rect.height - 52,
    )
    linhas = _quebrar_texto(fontes["pergunta"], pergunta_atual["pergunta"], texto_rect.width)
    _desenhar_texto_multilinha(tela, fontes["pergunta"], linhas, texto_rect)

    _desenhar_rodape(tela, fontes)


def desenhar_alternativas(tela, fontes, alternativas, rects, cores, indice_hover=None):
    """Desenha as quatro alternativas de resposta."""
    for indice, texto in enumerate(alternativas):
        rect = rects[indice]
        cor_fundo = cores[indice]

        if indice_hover == indice and cor_fundo == CORES["CARD"]:
            cor_fundo = CORES["HOVER"]

        _desenhar_card(tela, rect, cor_fundo)

        if cor_fundo == CORES["VERDE_FUNDO"]:
            cor_badge = CORES["VERDE_SUAVE"]
        elif cor_fundo == CORES["VERMELHO_FUNDO"]:
            cor_badge = CORES["VERMELHO_SUAVE"]
        else:
            cor_badge = CORES["DESTAQUE"]

        _desenhar_badge(tela, fontes, LETRAS_ALTERNATIVAS[indice], rect, cor_badge)

        texto_rect = pygame.Rect(
            rect.x + LARGURA_BADGE + 28,
            rect.y,
            rect.width - LARGURA_BADGE - 40,
            rect.height,
        )
        _desenhar_texto_em_rect(tela, fontes["alternativa"], texto, texto_rect, margem=0)


def desenhar_feedback(tela, fonte, acertou):
    """Mostra overlay e mensagem de feedback apos a resposta."""
    overlay = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
    overlay.fill(CORES["OVERLAY"])
    tela.blit(overlay, (0, 0))

    card_rect = pygame.Rect(LARGURA_TELA // 2 - 180, ALTURA_TELA // 2 - 60, 360, 120)

    if acertou:
        _desenhar_card(tela, card_rect, CORES["VERDE_FUNDO"], CORES["VERDE_SUAVE"], 3)
        _desenhar_texto_centralizado(
            tela,
            fonte,
            f"+{PONTOS_POR_ACERTO} pontos",
            card_rect.centery,
            CORES["VERDE_SUAVE"],
        )
    else:
        _desenhar_card(tela, card_rect, CORES["VERMELHO_FUNDO"], CORES["VERMELHO_SUAVE"], 3)
        _desenhar_texto_centralizado(
            tela,
            fonte,
            "Resposta incorreta",
            card_rect.centery,
            CORES["VERMELHO_SUAVE"],
        )


def desenhar_tela_final(tela, fontes, pontuacao):
    """Desenha a tela de encerramento com a pontuacao final."""
    _desenhar_fundo(tela)

    card_rect = pygame.Rect(LARGURA_TELA // 2 - 220, 150, 440, 300)
    _desenhar_card(tela, card_rect, CORES["CARD"])

    _desenhar_texto_centralizado(
        tela,
        fontes["final"],
        "Fim de jogo!",
        card_rect.y + 70,
        CORES["TEXTO"],
    )
    _desenhar_texto_centralizado(
        tela,
        fontes["titulo"],
        f"{pontuacao} pontos",
        card_rect.y + 150,
        CORES["DESTAQUE"],
    )
    _desenhar_texto_centralizado(
        tela,
        fontes["info"],
        "Pressione ESC para sair",
        card_rect.y + 230,
        CORES["TEXTO_SECUNDARIO"],
    )
