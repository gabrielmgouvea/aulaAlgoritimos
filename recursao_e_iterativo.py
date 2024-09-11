# def fatorialiterativo(n):
#     if n < 0:
#         return "nao pode utilizar número negativo!"
#     resultado = 1
#     for i in range(1, n+1):
#         resultado *= i
#     return resultado


# resultado = fatorialiterativo(int(input("insira um numero: ")))
# print(resultado)

# def fatRec(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * fatRec(n-1)
# resultado = fatRec(5)
# print(resultado)

# def potencia(base, expoente):
#     if expoente == 0:
#         return 1
#     elif expoente == 1:
#         return base
#     else:
#         return base * potencia(base, expoente - 1)

# resultado = potencia(3, 2)
# print(resultado)

# def Fibonacci(n):

#     if n < 0:
#         print("não pode inserir um negativo")
#     elif n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
# resultado = Fibonacci(9)
# print(resultado)
