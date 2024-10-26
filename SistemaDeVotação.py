import textwrap

lista_tarefas = []

def menu():
    menu = """
    Sistema de Votação
    As opções são:
    1. Opção 1
    2. Opção 2
    3. Opção 3
    Escolha uma opção (1-3) ou 0 para finalizar a votação: """
    return input(textwrap.dedent(menu))

def main():
    tarefas = []
    voto1 = 0
    voto2 = 0
    voto3 = 0
    while True:
        opcao = menu()

        if opcao == '1':
            voto1 += 1

        elif opcao == '2':
            voto2 += 2

        elif opcao == '3':
            voto3 += 3

        elif opcao == '0':
            print(f"Resultados da Votação:\nOpção 1: {voto1} voto(s)\nOpção 2: {voto2} voto(s)\nOpção 3: {voto3} voto(s)\n")
            break

        else:
            print("Operação inválida, tente novamente.")

main()
