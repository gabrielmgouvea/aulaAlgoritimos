#arquivos
import os
import textwrap

def menu():
    menu = """
    [1] Registrar evento
    [2] Visualizar log(s)
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def cria_arquivo():
    try:
        os.chdir(r'C:\Users\UNIVASSOURAS\Downloads\Aula')
        filename = input("Nome do arquivo: ")
        with open(filename, "w") as arquivo:
            arquivo.write(input("Descrição do evento: "))
            print("Arquivo criado!")

        with open('filename.txt',"r") as arquivo:
            conteudo = filename.read()
            print(conteudo)

    except FileNotFoundError:
        print("Arquivo nao encontrado")

    except PermissionError:
        print("Você nao tem permissao de leitura/escrita")

    except Exception as e:
        print(f"Deu erro de: {e}")

    finally:
        print("Até mais")


def main():

    while True:
        opcao = menu()

        if opcao == '1':
            cria_arquivo()

        elif opcao == '2':
            print("")

        elif opcao == 'q':
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, tente novamente.")

main()
