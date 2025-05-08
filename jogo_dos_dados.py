import random

print('Jogo dos Dados')

jogadores = int(input('Informe quantos vão jogar: '))
pontuacao = []

for c in range (jogadores):
    nome = str(input('Informe seu nome: '))

    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    total = dado1 + dado2

    print('o valor do dado 1 foi {} e o valor do dado 2 foi {}'.format(dado1,dado2))
    print('O resultado final foi de {} foi {}'.format(nome,total))
    pontuacao.append((nome,total))

print(pontuacao)

