notaA = float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

#calcular a média
media = (notaA + notaB) / 2

#verificando se o aluno foi aprovado ou reprovado
if media >= 7.0:
    print("Média: %.1f - Aprovado" % media)
else:
    print("Média: %.1f - Reprovado" % media)

#Mesma estrutura com elif:
if media >= 7.0:
    print("Média: %.1f - Aprovado" % media)
elif media >= 5.0:
    print("Média: %.1f - Recuperação" % media)
else:
    print("Média: %.1f - Reprovado" % media)
    