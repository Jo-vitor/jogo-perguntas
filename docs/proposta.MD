# Proposta Inicial do Jogo

Este documento deve ser preenchido pelo grupo na Semana 1 do projeto.

A proposta deve apresentar uma ideia simples, clara e viável para ser desenvolvida com Python e Pygame dentro do prazo disponível.

## 1. Nome provisório do jogo

> SportQuiz

## 2. Integrantes do grupo

- Nome 1: Arthur Lopes Teixeira
- Nome 2: Bernardo Duarte Medeiros de Paula
- Nome 3: Bernardo Machado Ribeiro
- Nome 4: João Vitor Soares

## 3. Tipo de jogo

Tipo escolhido pelo grupo:

> Jogo de perguntas e respostas.

## 4. Descrição geral do jogo

Descrição:

> Na tela principal aparecem perguntas de múltipla escolha sobre esportes (futebol, basquete, Fórmula 1, olimpíadas, entre outros). O jogador seleciona uma das quatro alternativas clicando com o mouse ou pressionando as teclas correspondentes. Cada pergunta tem um cronômetro individual: se o tempo acabar sem resposta, a pergunta é considerada errada. Ao final de todas as rodadas, a pontuação do jogador é registrada em um ranking local.

## 5. Objetivo do jogador

Objetivo:

> Responder o maior número possível de perguntas corretamente dentro do tempo limite, acumulando pontuação para alcançar a posição mais alta no ranking.

## 6. Regras principais

Regras do grupo:

- Regra 1: Cada pergunta tem um tempo limite de 15 segundos para ser respondida.
- Regra 2: Resposta correta dentro do tempo vale 100 pontos; resposta errada ou tempo esgotado vale 0 pontos.
- Regra 3: O jogo apresenta 10 perguntas por partida, selecionadas aleatoriamente do banco de questões.
- Regra 4: Não é possível voltar a uma pergunta já respondida ou pulada.
- Regra 5: Ao final da partida, a pontuação é registrada no ranking se estiver entre as 10 melhores.

## 7. Condição de vitória

Condição de vitória:

> O jogador vence (conclui o jogo com sucesso) ao responder todas as 10 perguntas da partida. A vitória é mais expressiva quanto maior for a pontuação acumulada e quanto melhor for a colocação no ranking.

## 8. Condição de derrota ou encerramento

Condição de derrota ou encerramento:

> A partida encerra automaticamente após as 10 perguntas serem respondidas ou o tempo de cada uma esgotar. Não há condição de derrota absoluta o jogador sempre completa a rodada, mas fica com pontuação zero se errar ou não responder todas as questões.

## 9. Elementos previstos no jogo

## Jogador ou elemento principal

Descrição:

> O jogador interage por meio do mouse (clique nas alternativas) ou pelas teclas 1, 2, 3 e 4 do teclado, correspondentes às quatro opções de resposta exibidas na tela.

## Obstáculos, inimigos ou desafios

Descrição:

> O principal desafio é o cronômetro regressivo exibido em destaque na tela. À medida que o jogo avança, perguntas mais difíceis aparecem com maior frequência, aumentando a pressão sobre o jogador.

## Itens, alvos ou objetos de interação

Descrição:

> As quatro alternativas de resposta são os elementos de interação principais. Ao selecionar a resposta correta, um feedback visual verde é exibido; ao errar, um feedback vermelho indica a alternativa correta.

## Pontuação, vidas, tempo ou progresso

Descrição:

> O jogador não possui vidas. A pontuação é acumulada ao longo das 10 perguntas (máximo de 1000 pontos por partida). Um indicador de progresso mostra a pergunta atual (ex.: "Pergunta 3 de 10"). O tempo restante de cada pergunta é exibido por uma barra que diminui visualmente.

## 10. Controles previstos

Controles do grupo:

- Tecla 1 / clique na opção A: selecionar primeira alternativa
- Tecla 2 / clique na opção B: selecionar segunda alternativa
- Tecla 3 / clique na opção C: selecionar terceira alternativa
- Tecla 4 / clique na opção D: selecionar quarta alternativa
- ESC: pausar o jogo / sair para o menu principal
- ENTER: confirmar na tela de menu ou ranking

## 11. Organização inicial do código

Organização planejada:

- `main.py`: inicializa o Pygame e chama o loop principal do jogo;
- `src/jogo.py`: contém o loop principal e a lógica de transição entre as telas;
- `src/config.py`: guarda constantes como tamanho da tela, cores, fontes e tempo limite por pergunta;
- `src/perguntas.py`: carrega e gerencia o banco de perguntas a partir do arquivo JSON;
- `src/ranking.py`: lê e grava o ranking em arquivo local (JSON ou TXT);
- `src/telas.py`: funções de renderização para cada tela (menu, pergunta, feedback, ranking);
- `data/perguntas.json`: banco de perguntas com enunciado, alternativas e resposta correta;
- `data/ranking.json`: armazena as pontuações registradas.

## 12. Recursos externos previstos

Recursos previstos:

- Fonte personalizada obtida de banco gratuito (Google Fonts);
- Sons de acerto e erro obtidos de banco de áudio gratuito (ex.: freesound.org);
- Banco de perguntas elaborado pelo próprio grupo.

## 13. Principais dificuldades esperadas

Dificuldades previstas:

- Dificuldade 1: Implementação do cronômetro por pergunta integrado ao loop do Pygame sem travar a interface.
- Dificuldade 2: Leitura e gravação do ranking em arquivo de forma confiável (tratamento de erros de I/O).
- Dificuldade 3: Organização do código em módulos separados mantendo a comunicação entre eles sem conflitos.

## 14. Escopo mínimo para a entrega final

Escopo mínimo:

> A versão mínima do jogo terá tela de menu inicial, 10 perguntas de múltipla escolha sobre esportes com cronômetro por questão, feedback visual de acerto/erro, sistema de pontuação e tela de encerramento exibindo a pontuação final e o ranking das 10 melhores pontuações salvas localmente.

## 15. Possíveis melhorias, caso haja tempo

Melhorias possíveis:

- Melhoria 1: Categorias de esportes selecionáveis no menu (futebol, basquete, olimpíadas etc.).
- Melhoria 2: Níveis de dificuldade (fácil, médio, difícil) com tempo e pontuação ajustados.
- Melhoria 3: Perguntas ilimitadas e adicionar vidas.