try:
    num = int(input("Valor: "))
    resultado = 100 / num
    print(resultado)
    
except ZeroDivisionError:
    print("não pode dividir por zero, caramba!")
except ValueError:
    print("Tipo errado, caramba!")
except Exception as e:
    print(f"Escreva o except{e}")
finally:
    print("Já era! Acabou! Boa sorte")
