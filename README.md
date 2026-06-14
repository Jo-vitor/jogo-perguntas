# SportQuiz

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido com Python e Pygame.

Este repositório é um template para os grupos da disciplina. A proposta é começar com uma base funcional e evoluir o jogo ao longo do semestre.

## Integrantes do grupo

- Arthur Lopes Teixeira
- Bernardo Duarte Medeiros de Paula
- Bernardo Machado Ribeiro
- João Vitor Soares

## Estrutura do projeto

- `main.py`: ponto de entrada da aplicação.
- `src/`: código-fonte principal do jogo (loop, regras, sprites e dados).
- `assets/`: imagens, fontes e sons.
- `data/`: arquivos persistentes (recorde/ranking).
- `tests/`: testes unitários com `pytest`.
- `docs/`: documentação do projeto, incluindo proposta inicial.

## Descrição do jogo

> Na tela principal aparecem perguntas de múltipla escolha sobre esportes (futebol, basquete, Fórmula 1, olimpíadas, entre outros). O jogador seleciona uma das quatro alternativas clicando com o mouse ou pressionando as teclas correspondentes. Cada pergunta tem um cronômetro individual: se o tempo acabar sem resposta, a pergunta é considerada errada. Ao final de todas as rodadas, a pontuação do jogador é registrada em um ranking local.

## Objetivo do jogador

> Responder o maior número possível de perguntas corretamente dentro do tempo limite, acumulando pontuação para alcançar a posição mais alta no ranking.

## Regras do jogo

- Cada pergunta tem um tempo limite de 15 segundos para ser respondida.
- Resposta correta dentro do tempo vale 100 pontos; resposta errada ou tempo esgotado vale 0 pontos.
- O jogo apresenta 10 perguntas por partida, selecionadas aleatoriamente do banco de questões.
- Não é possível voltar a uma pergunta já respondida ou pulada.
- Ao final da partida, a pontuação é registrada no ranking se estiver entre as 10 melhores.

## Controles

- Tecla 1 / clique na opção A: selecionar primeira alternativa
- Tecla 2 / clique na opção B: selecionar segunda alternativa
- Tecla 3 / clique na opção C: selecionar terceira alternativa
- Tecla 4 / clique na opção D: selecionar quarta alternativa
- Clique com o botão esquerdo do mouse: selecionar uma alternativa
- ESC: pausar o jogo / sair para o menu principal

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone LINK_DO_REPOSITORIO
cd NOME_DA_PASTA
pip install -r requirements.txt
python main.py
```

## Como executar os testes

```bash
python -m pytest
```

## Checklist mínimo para entrega

- Preencher este README com nome final, descrição real, regras e controles do jogo.
- Atualizar `docs/proposta.MD` com a proposta do grupo.
- Garantir que o jogo executa com `python main.py`.
- Garantir que os testes passam com `pytest`.

## Observações para os alunos

- Mantenham o código organizado em módulos pequenos e com responsabilidade clara.
- Comentem partes importantes da lógica, principalmente regras do jogo.
- Registrem decisões técnicas no README do grupo ao longo do desenvolvimento.
