notaA=float(input("Informe a primeira nota: "))
notaB=float(input("informe a segunda nota: "))
notaC=float(input("Informe a terceira nota: "))

#calcular media
mediafinal = (notaA + notaB + notaC) / 3

#verificação
if mediafinal >=7.0:
    print("A Média: %.1f - Aprovado" % mediafinal)
else:
    print("A Média: %.1f - Reprovado" % mediafinal)