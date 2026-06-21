import json
from pathlib import Path


def _criar_diretorio(caminho):
    Path(caminho).parent.mkdir(parents=True, exist_ok=True)


def carregar_perguntas_locais(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            perguntas = json.load(arquivo)
            return perguntas if isinstance(perguntas, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def carregar_recorde(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.read().strip()
            return int(conteudo) if conteudo else 0
    except (FileNotFoundError, ValueError):
        return 0


def salvar_recorde(caminho_arquivo, pontuacao):
    _criar_diretorio(caminho_arquivo)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(str(int(pontuacao)))


def carregar_ranking(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            return dados if isinstance(dados, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def adicionar_ranking(caminho_arquivo, pontuacao, max_itens=10):
    ranking = carregar_ranking(caminho_arquivo)
    ranking.append(int(pontuacao))
    ranking = sorted(ranking, reverse=True)[:max_itens]
    _criar_diretorio(caminho_arquivo)
    with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(ranking, arquivo, ensure_ascii=False, indent=2)
    return ranking
