from src.funcoes import calcular_pontos, verificar_resposta, limitar_valor


def test_calcular_pontos():
    """Deve somar corretamente os pontos atuais com os pontos ganhos."""
    assert calcular_pontos(10, 5) == 15


def test_verificar_resposta_correta():
    """Deve indicar resposta correta quando as alternativas batem."""
    assert verificar_resposta(2, 2) is True


def test_verificar_resposta_errada():
    """Deve indicar resposta incorreta quando os índices não batem."""
    assert verificar_resposta(1, 3) is False


def test_limitar_valor_abaixo_do_minimo():
    """Deve retornar o limite minimo quando o valor informado for menor."""
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    """Deve retornar o limite maximo quando o valor informado for maior."""
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    """Deve manter o valor original quando ele ja estiver no intervalo."""
    assert limitar_valor(50, 0, 100) == 50
