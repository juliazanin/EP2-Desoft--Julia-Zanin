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


#partida completa
def joga_uma_partida(base_por_nivel, nome_jogador):
    premio_atual = 0
    pulos_restantes = PULOS_INICIAIS
    ajudas_restantes = AJUDAS_INICIAIS
    sorteadas = []
    indice_pergunta = 0
 
    for nivel in NIVEL_PERGUNTA:
        premio_da_pergunta = PREMIOS[indice_pergunta]
        cor = cor_do_premio(premio_da_pergunta)
 
        print(f"\n{cor}{NEGRITO}Prêmio atual: R$ {premio_atual}{RESET}")
        print(f"{cor}Pergunta de R$ {premio_da_pergunta} (nível {nivel}){RESET}")
 
        questao = sorteia_questao_inedita(base_por_nivel, nivel, sorteadas)
        ajuda_usada_na_pergunta = False
        opcao = None
        resposta_definida = False
 
        while not resposta_definida:  # repete enquanto o jogador pular ou pedir ajuda
            print(questao_para_texto(questao, indice_pergunta + 1))
 
            opcao = pede_opcao(pulos_restantes, ajudas_restantes, ajuda_usada_na_pergunta)
 
            if opcao == "PULA":
                pulos_restantes -= 1
                questao = sorteia_questao_inedita(base_por_nivel, nivel, sorteadas)
                ajuda_usada_na_pergunta = False
            elif opcao == "AJUDA":
                ajuda= gera_ajuda(questao)
                print(f"{AMARELO}{ajuda}{RESET}")
                ajudas_restantes -= 1
                ajuda_usada_na_pergunta = True
            else:  # opcao é A, B, C ou D
                resposta_definida = True  
 
        if opcao == questao["correta"]:
            premio_atual = premio_da_pergunta
            print(f"{VERDE}{NEGRITO}Resposta correta! Prêmio: R$ {premio_atual}{RESET}")
 
            if premio_atual == PREMIOS[-1]:
                print(f"\n{VERDE}{NEGRITO}PARABÉNS, {nome_jogador}! "
                      f"Você ganhou o prêmio máximo de R$ {premio_atual}!{RESET}")
                return premio_atual
 
            if not pergunta_sim_ou_nao("Deseja continuar jogando?"):
                print(f"\n{CIANO}Você decidiu parar. Saiu com R$ {premio_atual}!{RESET}")
                return premio_atual
        else:
            print(f"{VERMELHO}{NEGRITO}Resposta errada! A correta era {questao['correta']}.{RESET}")
            print(f"{VERMELHO}Você saiu sem nenhum prêmio, {nome_jogador}!{RESET}")
            return 0
 
        indice_pergunta += 1
 
    return premio_atual