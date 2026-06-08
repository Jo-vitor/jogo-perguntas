import pygame

from src.config import (
    LARGURA_TELA,
    ALTURA_TELA,
    TITULO_JOGO
)
from src.funcoes import (
    desenhar_inico_jogo,
    criar_resposta,
    selecionar_resposta
)

def executar_jogo():
    """Executa o loop principal do jogo e controla estado, colisões e pontuação."""
    pygame.init()
    

    tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption(TITULO_JOGO)

    rodando = True

    respostas = criar_resposta()
    
    while rodando:
        desenhar_inico_jogo(tela, respostas)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False
            selecionar_resposta(evento)

        pygame.time.wait(1)
        pygame.display.flip()
        

    pygame.quit()