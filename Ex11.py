largura = float(input("informe a largura da parede: "))
altura = float(input("Informe a altura da parede: "))
area = largura * altura
print("Sua parede tem a dimensão de {}x{} e a sua área é de {}m².".format(largura,altura,area))
tinta = area / 2
print("E vai precissar {}L para pintar essa parede. ".format(tinta))
