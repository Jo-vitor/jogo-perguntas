def calcular_pontos(pontos_atual, pontos_ganhos):
    """Soma os pontos ganhos à pontuação atual."""
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    """Reduz a vida atual com base no dano recebido."""
    return vida_atual - dano


def jogador_perdeu(vidas):
    """Indica se o jogador ficou sem vidas."""
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    """Mantém um valor dentro do intervalo [minimo, maximo]."""
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    """Verifica sobreposição entre dois retângulos do Pygame."""
    return retangulo_1.colliderect(retangulo_2)


def verificar_resposta(resposta_jogador, resposta_correta):
    """Retorna True quando a resposta do jogador corresponde à resposta correta."""
    return resposta_jogador == resposta_correta


def formatar_tempo(segundos):
    """Retorna o tempo em segundos formatado como MM:SS."""
    if segundos < 0:
        segundos = 0
    minutos = int(segundos) // 60
    segundos_inteiros = int(segundos) % 60
    return f"{minutos:02d}:{segundos_inteiros:02d}"
