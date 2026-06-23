quantidade = 0
soma = 0
media = 0
valor = float(input("Digite um valor (ou -1 para sair): "))

while valor != -1:
    soma += valor
    quantidade += 1
    valor = float(input("Digite um valor (ou -1 para sair): "))

#para encerrar o loop, o usuário deve digitar -1
media = soma / quantidade
print("\nTotal da soma dos valores: ", soma)
print("\nQuantidade de valores digitados: ", quantidade)
print("\nMédia dos valores: ", "%.1f" % media)