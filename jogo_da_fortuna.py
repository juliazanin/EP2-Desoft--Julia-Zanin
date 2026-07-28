#importa as funções auxiliares
from funcoes import (
    transforma_base,
    valida_questao,
    valida_questoes,
    sorteia_questao,
    sorteia_questao_inedita,
    questao_para_texto,
    gera_ajuda,
)
from perguntas import questoes as perguntas
from tela import (
    RESET,
    NEGRITO,
    VERDE,
    AMARELO,
    VERMELHO,
    CIANO,
    MAGENTA,
    cor_do_premio,
    exibe_manual,
    pede_nome,
    pede_opcao,
    pergunta_sim_ou_nao,
)

# Configurações dos estados iniciais do jogo
PREMIOS = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]
NIVEL_PERGUNTA = ["facil", "facil", "facil", "medio", "medio", "medio", "dificil", "dificil", "dificil"]
 
PULOS_INICIAIS = 3
AJUDAS_INICIAIS = 2


# Validação das questões usando a função auxiliar
def valida_base(lista_questoes):
    resultados = valida_questoes(lista_questoes)
    tem_erro = False
    i = 0
    for erro in resultados:
        if erro:
            tem_erro = True
            print(f"{VERMELHO}Problema na questão {i}: {erro}{RESET}")
        i += 1
    if tem_erro:
        return False
    else:
        return True
    
 
 
