import json
from random import sample


def carregar_perguntas(caminho_arquivo):
    """Carrega perguntas de um arquivo JSON e retorna uma lista de dicionários."""
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            perguntas = json.load(arquivo)
            return perguntas if isinstance(perguntas, list) else []
    except FileNotFoundError:
        return []


def selecionar_perguntas(perguntas, quantidade):
    """Seleciona um subconjunto de perguntas de forma aleatória."""
    if not perguntas:
        return []
    if len(perguntas) <= quantidade:
        return perguntas.copy()
    return sample(perguntas, quantidade)
