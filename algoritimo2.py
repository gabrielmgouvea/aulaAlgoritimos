import math
def somatorio():
    n = int(input("Insira um número: "))
    i = 1
    soma = 0
    for i in range(n):
        i = i + 1
        soma += math.pow((i + 1),2)
    return soma
resultado = somatorio()
print(resultado)