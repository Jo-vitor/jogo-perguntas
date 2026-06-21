# SportQuiz

Projeto final da disciplina de Introdução a Algoritmos/Programação, desenvolvido em Python com a biblioteca Pygame.

O SportQuiz é um jogo de perguntas e respostas sobre esportes. O jogador responde perguntas de múltipla escolha dentro de um tempo limite, acumula pontos ao acertar e tenta alcançar uma boa posição no ranking local.

O projeto foi desenvolvido a partir do template oficial da disciplina, mantendo a estrutura inicial de pastas e arquivos, mas com adaptações para a proposta do grupo.

## Integrantes do grupo

* Arthur Lopes Teixeira
* Bernardo Duarte Medeiros de Paula
* Bernardo Machado Ribeiro
* João Vitor Soares

## Descrição do jogo

Na tela principal, o jogador pode iniciar uma partida, visualizar o ranking ou sair do jogo.

Durante a partida, aparecem perguntas de múltipla escolha sobre esportes, como futebol, basquete, Fórmula 1, Olimpíadas e outros temas relacionados. Cada pergunta possui quatro alternativas, e o jogador deve escolher a resposta correta usando o teclado ou o mouse.

Cada pergunta tem um tempo limite. Se o jogador acertar, recebe pontos. Se errar ou deixar o tempo acabar, não recebe pontuação naquela pergunta. Ao final da partida, a pontuação é exibida e registrada em um ranking local.

## Objetivo do jogador

Responder o maior número possível de perguntas corretamente dentro do tempo limite, acumulando pontuação para superar o recorde e alcançar uma boa posição no ranking.

## Regras do jogo

* Cada partida possui 10 perguntas;
* As perguntas são selecionadas a partir de um banco salvo em arquivo JSON;
* Cada pergunta possui 4 alternativas;
* Apenas uma alternativa está correta;
* Cada pergunta tem tempo limite de 15 segundos;
* Resposta correta vale 100 pontos;
* Resposta errada ou tempo esgotado vale 0 pontos;
* Não é possível voltar para uma pergunta já respondida;
* Ao final da partida, a pontuação é registrada no ranking local;
* O ranking mantém as melhores pontuações salvas no computador.

## Controles

### Menu

* `W` ou seta para cima: mover seleção para cima;
* `S` ou seta para baixo: mover seleção para baixo;
* `ENTER`: selecionar opção;
* `ESC`: voltar ou sair.

### Durante a partida

* `1`: selecionar a primeira alternativa;
* `2`: selecionar a segunda alternativa;
* `3`: selecionar a terceira alternativa;
* `4`: selecionar a quarta alternativa;
* Clique com o botão esquerdo do mouse: selecionar uma alternativa;
* `ESC`: sair ou voltar, dependendo da tela.

## Mecânicas implementadas

* Janela do Pygame funcionando;
* Menu inicial;
* Tela principal de perguntas;
* Controle por teclado;
* Controle por mouse;
* Perguntas de múltipla escolha;
* Sistema de pontuação;
* Tempo limite por pergunta;
* Feedback visual de resposta correta ou incorreta;
* Tela final com pontuação;
* Recorde salvo em arquivo local;
* Ranking salvo em arquivo local;
* Banco de perguntas em arquivo JSON;
* Testes simples com pytest;
* Código organizado em módulos e funções.

## Conceitos da disciplina utilizados

O projeto utiliza os seguintes conceitos trabalhados na disciplina:

* Variáveis;
* Entrada e saída de dados;
* Estruturas condicionais;
* Laços de repetição;
* Listas;
* Dicionários;
* Tuplas;
* Funções;
* Modularização;
* Leitura de arquivos;
* Escrita de arquivos;
* Manipulação de dados em JSON;
* Testes automatizados;
* Organização de código em pastas e módulos.

## Estrutura do projeto

```txt
jogo-perguntas/
├── assets/
├── data/
│   ├── perguntas.json
│   ├── ranking.json
│   └── recorde.txt
├── docs/
│   └── proposta.md
├── src/
│   ├── config.py
│   ├── engine.py
│   ├── funcoes.py
│   ├── perguntas.py
│   ├── screens/
│   │   └── ui.py
│   └── services/
│       └── data_service.py
├── tests/
│   └── test_logica.py
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Principais arquivos

* `main.py`: ponto de entrada da aplicação;
* `src/engine.py`: controla o loop principal, os estados do jogo e a lógica geral da partida;
* `src/config.py`: armazena constantes e configurações do jogo;
* `src/funcoes.py`: contém funções auxiliares de lógica;
* `src/perguntas.py`: contém funções relacionadas ao carregamento e seleção de perguntas;
* `src/screens/ui.py`: contém as funções responsáveis por desenhar as telas e elementos visuais;
* `src/services/data_service.py`: realiza leitura e escrita de dados em arquivos;
* `data/perguntas.json`: banco de perguntas do jogo;
* `data/recorde.txt`: arquivo que armazena o recorde local;
* `data/ranking.json`: arquivo que armazena as melhores pontuações;
* `tests/test_logica.py`: testes simples para funções de lógica do projeto;
* `docs/proposta.md`: proposta inicial do jogo.

## Como executar o projeto

Primeiro, instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, execute o jogo:

```bash
python main.py
```

## Como executar os testes

Para rodar os testes automatizados, execute:

```bash
python -m pytest
```

## Arquivos auxiliares

O jogo utiliza arquivos auxiliares para armazenar e carregar informações importantes:

* `data/perguntas.json`: contém as perguntas e alternativas usadas no jogo;
* `data/recorde.txt`: armazena o maior recorde local;
* `data/ranking.json`: armazena as melhores pontuações.

Esses arquivos devem permanecer no repositório para que o jogo funcione corretamente.

## Recursos externos

O projeto utiliza a biblioteca Pygame para criação da interface gráfica e execução do jogo.

O projeto foi desenvolvido a partir do template oficial da disciplina. As perguntas foram elaboradas pelo grupo. Os arquivos presentes na pasta `assets/` fazem parte da estrutura do projeto/template ou foram mantidos como recursos auxiliares.

Caso algum recurso externo seja adicionado ao projeto, como imagens, sons ou fontes, sua origem e licença devem ser informadas nesta seção.

## Status da entrega

O jogo está em sua versão final para a entrega da Semana 4. Ele está funcional, executável, com interface gráfica, sistema de perguntas, pontuação, tempo, recorde, ranking local, documentação e testes implementados.
