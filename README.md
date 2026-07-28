# EP2-Desoft--Julia-Zanin
Exercício de Programa 2 Desoft- Julia Zanin

# Fortuna DesSoft
Jogo de perguntas e respostas no estilo "Show do Milhão", feito em Python para o exercício programa 2 (EP) da disciplina Desing de Software, do Insper.

## Proposito
O jogador responde perguntas de múltipla escolha (A, B, C ou D) e, a cada acerto, o prêmio aumenta. Se errar, perde tudo e a partida acaba na hora. O objetivo é chegar ao prêmio máximo de R$ 1.000.000, respondendo 9 perguntas seguidas corretamente, ou parar em algum ponto e sair com o valor já conquistado.
Os valores do prêmio, em ordem, são:
R$ 1.000, R$ 5.000, R$ 10.000, R$ 30.000, R$ 50.000, R$ 100.000, R$ 300.000, R$ 500.000, R$ 1.000.000.

As 3 primeiras perguntas são de nível fácil, as 3 seguintes de nível médio, e as 3 últimas de nível difícil.

## Como jogar
1. Ao iniciar, o jogo pede o nome do jogador e exibe um manual rápido com as regras.
2. Em cada pergunta, o jogador escolhe uma das opções digitando A, B, C ou D.
3. Também é possível digitar PULA para trocar a pergunta atual por outra do mesmo nível, sem gastar uma tentativa de resposta. O jogador tem 3 pulos no total, para o jogo inteiro.
4. Também é possível digitar AJUDA para eliminar uma ou duas opções sabidamente erradas. O jogador tem 2 ajudas no total, e não pode pedir ajuda mais de uma vez na mesma pergunta.
5. Se a resposta estiver correta, o prêmio sobe para o valor da pergunta atual, e o jogador pode escolher entre continuar jogando ou parar e sair com o prêmio já conquistado.
6. Se a resposta estiver errada, o jogo termina e o jogador sai sem nenhum prêmio.
7. Ao chegar em R$ 1.000.000, o jogo termina automaticamente com uma mensagem de vitória.
8. Ao final de cada partida, o jogo pergunta se o jogador quer jogar de novo, sem precisar executar o programa outra vez.

## Como rodar no terminal
O jogo precisa dos arquivos `funcoes.py`, `perguntas.py`, `tela.py` e `jogo_da_fortuna.py` na mesma pasta.
1. Abra o terminal e entre na pasta do projeto:
```
cd caminho/da/pasta/EP2-Desoft--Julia-Zanin
```

2. Rode o arquivo principal com Python 3:
```
python3 jogo_da_fortuna.py
```

Em alguns sistemas o comando pode ser `python` em vez de `python3`.

3. Siga as instruções que aparecem na tela para jogar.
## Estrutura dos arquivos
- `funcoes.py`: as funções obrigatórias do jogo (validação da base de perguntas, sorteio de perguntas e geração de ajuda).
- `perguntas.py`: a base de perguntas usada no jogo.
- `tela.py`: as funções de entrada e saída (mensagens exibidas ao jogador e leitura das respostas digitadas).
- `jogo_da_fortuna.py`: o programa principal, que junta as funções acima e conduz o fluxo do jogo.