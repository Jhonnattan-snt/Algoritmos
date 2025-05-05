km = int(input("Qual a distância de KM percorridos? "))
dia = int(input("Quantos dias o carro foi alugado? "))
aluguel = (dia * 60) + (km * 0.15)
print("O aluguel do carro ficou de {}".format(aluguel))