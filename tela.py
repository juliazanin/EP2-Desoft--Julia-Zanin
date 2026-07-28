
#cores da tela e validação das entradas
RESET = "\033[0m"
NEGRITO = "\033[1m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
VERMELHO = "\033[91m"
CIANO = "\033[96m"
MAGENTA = "\033[95m"


#cores diferentes para cada prêmio
def cor_do_premio(valor):
    if valor < 10000:
        return VERDE
    if valor < 100000:
        return CIANO
    if valor < 500000:
        return AMARELO
    return VERMELHO

#manual do jogo
def exibe_manual(pulos_iniciais, ajudas_iniciais,nome):
    print(f"\n{NEGRITO}{CIANO}=== BEM-VINDO AO FORTUNA DESSOFT ==={RESET}")
    print("Responda às perguntas corretamente e leve para casa R$ 1.000.000!")
    print("A cada pergunta, escolha uma das opções: A, B, C ou D.")
    print(f"Você também pode digitar {NEGRITO}PULA{RESET} para trocar de pergunta")
    print(f"(você tem {pulos_iniciais} pulos) ou {NEGRITO}AJUDA{RESET} para eliminar")
    print(f"respostas erradas (você tem {ajudas_iniciais} ajudas no total do jogo).")
    print(f"Se errar uma pergunta, você perde tudo! Boa sorte {nome}!\n")


#pede o nome do jogador
def pede_nome():
    nome = input("Qual é o seu nome? ")
    nome= nome.strip()
    while nome == "":
        nome = input("Digite um nome válido: ").strip()
    return nome

#verifica se a resposta dada pelo jogador na pergunta é válida (deve ser A, B, C, D, PULA ou AJUDA)
def pede_opcao(pulos_restantes, ajudas_restantes, ajuda_usada_na_pergunta):
    opcao_valida = None

    while opcao_valida is None:
        entrada = input("\nQual a sua resposta (A/B/C/D), ou digite PULA / AJUDA: ")
        entrada= entrada.strip() #tira espaços
        entrada= entrada.upper() #deixa em letra maiúscula

        if entrada in ("A", "B", "C", "D"):
            opcao_valida = entrada
        elif entrada == "PULA" and pulos_restantes > 0:
            opcao_valida = "PULA"
        elif entrada == "PULA" and pulos_restantes <=0:
            print(f"{VERMELHO}Você não tem mais pulos disponíveis!{RESET}")
        elif entrada == "AJUDA" and ajuda_usada_na_pergunta:
            print(f"{VERMELHO}Você já pediu ajuda nesta pergunta!{RESET}")
        elif entrada == "AJUDA" and ajudas_restantes > 0:
            opcao_valida = "AJUDA"
        elif entrada == "AJUDA" and ajudas_restantes <=0:
            print(f"{VERMELHO}Você não tem mais ajudas disponíveis!{RESET}")
        else:
            print(f"{VERMELHO}Opção inválida! Digite A, B, C, D, PULA ou AJUDA para responder a pergunta.{RESET}")

    return opcao_valida


#verifica se perguntas de S ou N são válidas
def pergunta_sim_ou_nao(texto):
    resposta_valida = None
    while resposta_valida is None:
        resposta = input(f"\n{texto} (S/N): ")
        resposta=resposta.strip()
        resposta= resposta.upper()
        if resposta in ("S", "N"):
            resposta_valida = resposta
        else:
            print(f"{VERMELHO}Digite apenas S ou N.{RESET}")
    return resposta_valida == "S"