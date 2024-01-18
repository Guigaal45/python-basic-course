def lernotas():
    n=float(input('Digite uma nota para o aluno(a): '))
    return n


def resultado(n1, n2):
    média=(n1+n2)/2
    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    #print("Nota 3: ", n3)
    print("Média: ", média, "Resultado: ", end="")
    if média >= 6:
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
#c = lernotas()
resultado(a, b)