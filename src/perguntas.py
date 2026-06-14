import json
import random


def carregar_perguntas(caminho):
    """Carrega o banco de perguntas a partir de um arquivo JSON."""
    with open(caminho, "r", encoding="utf-8") as arquivo:
        perguntas = json.load(arquivo)

    for pergunta in perguntas:
        if len(pergunta["alternativas"]) != 4:
            raise ValueError("Cada pergunta deve ter exatamente 4 alternativas.")

        if not 0 <= pergunta["correta"] <= 3:
            raise ValueError("O indice da resposta correta deve estar entre 0 e 3.")

    return perguntas


def selecionar_perguntas(lista, quantidade=10):
    """Embaralha e retorna ate a quantidade solicitada de perguntas."""
    copia = lista.copy()
    random.shuffle(copia)
    return copia[:quantidade]
