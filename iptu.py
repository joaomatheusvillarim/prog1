area, aliquota = float(input("Área construída? ")), float(input("Alíquota? "))
valor = area*aliquota + 35
print("IPTU: R$ {:.2f}\n\nPagamento:\n1. Quota única. R$ {:.2f}".format(valor, valor*0.75))
print("2. Em 6 parcelas. Total: R$ {:.2f}\n   6 x R$ {:.2f}\n3. Em 10 parcelas. Total: R$ {:.2f}\n   10 x R$ {:.2f}".format(valor*0.95, (valor*0.95)/6, valor, valor/10))