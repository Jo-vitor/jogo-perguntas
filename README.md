# SportQuiz

SportQuiz é um jogo de perguntas e respostas sobre esportes desenvolvido em Python com a biblioteca Pygame. O projeto foi criado como entrega final da disciplina de Introdução aos Algoritmos, utilizando o template oficial disponibilizado pelo professor.

O objetivo do jogo é testar os conhecimentos do jogador sobre esportes por meio de perguntas de múltipla escolha. A cada rodada, o jogador deve escolher a alternativa correta antes que o tempo acabe. Respostas corretas aumentam a pontuação, e ao final da partida o resultado é salvo em um ranking local.

## Integrantes

* Arthur Lopes Teixeira
* Bernardo Duarte Medeiros de Paula
* Bernardo Machado Ribeiro
* João Vitor Soares

## Proposta do jogo

O SportQuiz é um jogo simples, funcional e jogável, com foco na aplicação dos principais conceitos estudados na disciplina. O jogador interage com perguntas de múltipla escolha, acumula pontos ao acertar respostas e tenta superar seu próprio recorde.

A partida termina quando todas as perguntas da rodada são respondidas. Ao final, o jogo exibe a pontuação final, atualiza o recorde local e registra o desempenho no ranking.

## Como jogar

Na tela inicial, o jogador pode iniciar uma partida, visualizar o ranking ou sair do jogo.

Durante a partida:

* Cada pergunta possui quatro alternativas;
* O jogador deve escolher uma alternativa usando o teclado ou o mouse;
* Respostas corretas somam pontos;
* Cada pergunta possui tempo limite;
* Ao final da rodada, a pontuação é exibida na tela final;
* O ranking local armazena as melhores pontuações.

## Controles

### Menu

* `W` ou seta para cima: mover seleção para cima;
* `S` ou seta para baixo: mover seleção para baixo;
* `ENTER`: selecionar opção;
* `ESC`: voltar ou sair.

### Durante o jogo

* `1`, `2`, `3`, `4`: selecionar alternativa;
* Clique do mouse: selecionar alternativa;
* `ESC`: sair ou voltar, dependendo da tela.

## Mecânicas implementadas

* Janela do Pygame funcionando;
* Menu inicial com opções de navegação;
* Tela principal de perguntas;
* Controle por teclado e mouse;
* Perguntas de múltipla escolha;
* Sistema de pontuação;
* Tempo limite por pergunta;
* Feedback visual de resposta correta ou incorreta;
* Recorde salvo em arquivo local;
* Ranking salvo em arquivo local;
* Tela final de resultado;
* Código organizado em módulos e funções;
* Leitura de perguntas a partir de arquivo JSON;
* Escrita e leitura de recorde e ranking em arquivos locais;
* Testes simples para funções de lógica do jogo.

## Conceitos da disciplina utilizados

O projeto aplica os seguintes conceitos estudados ao longo da disciplina:

* Variáveis;
* Entrada e saída de dados;
* Estruturas condicionais;
* Laços de repetição;
* Listas;
* Dicionários;
* Tuplas;
* Funções;
* Modularização;
* Manipulação de arquivos;
* Leitura de dados em JSON;
* Escrita de dados em arquivos locais;
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
└── requirements.txt
```

## Descrição dos principais arquivos

* `main.py`: ponto de entrada do projeto. Inicia a execução do jogo;
* `src/engine.py`: controla o loop principal, os estados do jogo e a lógica geral da partida;
* `src/config.py`: armazena configurações gerais, como tamanho da tela, cores, caminhos de arquivos e constantes do jogo;
* `src/funcoes.py`: contém funções auxiliares de lógica;
* `src/perguntas.py`: contém funções relacionadas às perguntas do jogo;
* `src/screens/ui.py`: contém funções responsáveis por desenhar as telas, botões, textos e elementos visuais;
* `src/services/data_service.py`: realiza leitura e escrita de dados, como perguntas, recorde e ranking;
* `data/perguntas.json`: arquivo com o banco de perguntas;
* `data/recorde.txt`: arquivo que armazena o maior recorde local;
* `data/ranking.json`: arquivo que armazena as melhores pontuações;
* `docs/proposta.md`: proposta inicial do jogo;
* `tests/test_logica.py`: testes simples para validar funções de lógica do projeto;
* `requirements.txt`: lista de dependências necessárias para executar o projeto.

## Como executar o jogo

Primeiro, instale as dependências:

```bash
pip install -r requirements.txt
```

Depois, execute o jogo:

```bash
python main.py
```

## Como executar os testes

Para executar os testes automatizados, use o comando:

```bash
python -m pytest
```

## Arquivos auxiliares

O jogo utiliza arquivos auxiliares para armazenar e carregar informações importantes:

* `data/perguntas.json`: contém as perguntas e alternativas usadas durante a partida;
* `data/recorde.txt`: armazena o maior recorde atingido;
* `data/ranking.json`: armazena as melhores pontuações do jogador.

Esses arquivos são necessários para o funcionamento correto do jogo e devem ser mantidos no repositório.

## Regras do jogo

* O jogador inicia uma partida pelo menu principal;
* Cada pergunta apresenta quatro alternativas;
* Apenas uma alternativa está correta;
* O jogador pode responder usando teclado ou mouse;
* Cada resposta correta soma pontos;
* Cada pergunta possui tempo limite;
* A partida termina quando todas as perguntas da rodada são respondidas;
* Ao final, o jogo exibe a pontuação final, atualiza o recorde e salva o resultado no ranking.

## Condição de encerramento

A partida é encerrada quando o jogador responde todas as perguntas selecionadas para a rodada. Após isso, o jogo apresenta a tela final com a pontuação obtida e o recorde atual.

## Recursos externos

O projeto utiliza a biblioteca Pygame para criação da interface gráfica e execução do jogo.

O projeto foi desenvolvido a partir do template oficial da disciplina, mantendo a organização inicial de pastas e arquivos proposta pelo professor.

As perguntas foram elaboradas pelo grupo. Os arquivos presentes na pasta `assets/` fazem parte da estrutura do projeto/template ou foram mantidos como recursos auxiliares. Caso novos recursos externos sejam adicionados, como imagens, sons ou fontes, sua origem e licença devem ser registradas nesta seção.

## Observações finais

O SportQuiz foi desenvolvido com foco em simplicidade, organização e funcionamento correto. A proposta prioriza um jogo pequeno, jogável e bem estruturado, de acordo com os requisitos da entrega final do trabalho prático.
