try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"O resultado é: {resultado}")

except ZeroDivisionError:
    print("Não pode dividir por zero, caramba!")
except ValueError:
    print("Tipo errado, caramba! Insira apenas números inteiros.")
finally:
    print("Tentativa de divisão finalizada.")
