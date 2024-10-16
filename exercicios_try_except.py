print("Questão 1\n")
try:
    num = int(input("Valor: "))
    resultado = 100 / num
    print(resultado)
    
except ZeroDivisionError:
    print("não pode dividir por zero, caramba!")
except ValueError:
    print("Tipo errado, caramba!")
finally:
    print("Já era! Acabou! Boa sorte\n")


print("Questão 2\n") 
  
import matplotlib.colors as mcolors
def rgb(cor_nome):
    try:
        cor_hex = mcolors.CSS4_COLORS[cor_nome]
        cor_rgb = tuple(int(cor_hex[i:i+2], 16) for i in (1, 3, 5))
        return {cor_nome: cor_rgb}
    except KeyError:
        raise ValueError(f"Cor '{cor_nome}' não encontrada.\n")

cor_nome = input("Digite o nome da cor: ").lower()

try:
    resultado = rgb(cor_nome)
    print(f"{resultado}\n")
except ValueError as e:
    print(e)

print("Questão 3\n")

try:
    num = int(input("Insira um numero: "))
    if num > 10:
        print("Numero valido!")
    else:
        print("Programa executado com sucesso, porém, o numero inserido é invalido")

except ValueError:
    print("Tipo errado, caramba!")
finally:
    print("Programa encerrado\n")

print("Questão 4\n")
