#exercicio 1
def transforma_base (questoes):
    dicionario={}
    for questao in questoes:
        nivel= questao["nivel"]
        if nivel not in dicionario:
            dicionario[nivel]=[]
        dicionario[nivel].append(questao)
        
    return dicionario