from src.funcoes import calcular_pontos, verificar_resposta


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_calcular_pontos_acerto():
    """Deve somar 100 pontos quando o jogador acerta uma pergunta."""
    assert calcular_pontos(200, 100) == 300


def test_verificar_resposta_correta():
    """Deve retornar True quando a alternativa selecionada e a correta."""
    assert verificar_resposta(2, 2) is True


def test_verificar_resposta_errada():
    """Deve retornar False quando a alternativa selecionada esta errada."""
    assert verificar_resposta(1, 3) is False
