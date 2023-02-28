identificador, horario, assento, portao, x, y = input(), input(), input(), input(), float(input()), float(input())
imposto = (1 - x/y)*100
print(f"### Cartão de Embarque ###\nIdentificador do voo: {identificador}\nHorário: {horario}\nAssento: {assento}\nPortão: {portao}\nTotal de Imposto: {imposto:.1f}%")