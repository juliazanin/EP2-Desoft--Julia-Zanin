#exercicio 1
def transforma_base (questoes):
    dicionario={}
    for questao in questoes:
        nivel= questao["nivel"]
        if nivel not in dicionario:
            dicionario[nivel]=[]
        dicionario[nivel].append(questao)
        
    return dicionario

#exercicio 2
def valida_questao(questao):
    saida={}
    chaves=["titulo", "nivel","opcoes","correta"]
    for chave in chaves:
        if chave not in questao:
            saida[chave]="nao_encontrado"

    if len(questao)!=4:
        saida["outro"]= "numero_chaves_invalido"

    if "titulo" in questao:
        titulo= questao["titulo"].strip()
        if titulo=="":
            saida["titulo"]="vazio"

    if "nivel" in questao:
        if questao["nivel"]!="facil" and questao["nivel"]!="medio" and questao["nivel"]!="dificil": #ou if questao["nivel"] not in ["facil", "medio","dificil"]
                saida["nivel"]= "valor_errado"

    if "opcoes" in questao:
        opcoes = questao["opcoes"]
        if len(opcoes)!=4:
            saida["opcoes"]= "tamanho_invalido"
        else:
            for opcao in opcoes:
                if opcao!="A" and opcao!="B" and  opcao!="C" and opcao!="D": #ou if opcao not in ["A","B","C","D"]
                    saida["opcoes"]= "chave_invalida_ou_nao_encontrada"
                else:
                    for opcao in opcoes:
                        if opcoes[opcao].strip() == "":
                            if "opcoes" not in saida:
                                saida["opcoes"]={}
                            saida["opcoes"][opcao]="vazia"

    if "correta" in questao:
        if questao["correta"]!="A" and questao["correta"]!="B" and questao["correta"]!="C" and questao["correta"]!="D":
            saida["correta"]="valor_errado"
    
    return saida


#exercicio 3
def valida_questoes (lista):
    final= []
    for questao in lista:
        saida= valida_questao(questao)
        final.append(saida)
    return final

#exercicio 4
import random 
def sorteia_questao (questoes,nivel):
    opcoes= questoes[nivel] #lista de questoes(representadas por dicionarios) daquele nivel
    indice_sorteada= random.randint(0, len(opcoes) - 1)
    return opcoes[indice_sorteada]

#exercicio 5
def sorteia_questao_inedita (questoes,nivel,sorteadas):
    questao_sorteada= sorteia_questao(questoes,nivel)
    while questao_sorteada in sorteadas:
        questao_sorteada= sorteia_questao(questoes,nivel)

    sorteadas.append(questao_sorteada)
    return questao_sorteada

#exercicio 6
def questao_para_texto (questao, id):
    pergunta= questao["titulo"]
    opcaoA= questao["opcoes"]["A"]
    opcaoB= questao["opcoes"]["B"]
    opcaoC= questao["opcoes"]["C"]
    opcaoD= questao["opcoes"]["D"]

    string= f"----------------------------------------\nQUESTAO {id}\n\n{pergunta}\n\nRESPOSTAS:\nA: {opcaoA}\nB: {opcaoB}\nC: {opcaoC}\nD: {opcaoD}"
    return string