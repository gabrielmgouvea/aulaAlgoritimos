#arquivos
import os
def cria_arquivo():
    try:
        os.chdir(r'C:\Users\UNIVASSOURAS\Downloads\Aula')
        with open("arquivo.txt","w") as arquivo:
            arquivo.write("escrevendo alguma coisa\nescrevendo outra coisa")
            
        with open("arquivo.txt","r") as arquivo:
            conteudo = arquivo.read()
            print(conteudo)

        # print(os.getcwd())

    except FileNotFoundError:
        print("Arquivo nao encontrado")

    except PermissionError:
        print("Você nao tem permissao de leitura/escrita")

    except Exception as e:
        print(f"Deu erro de: {e}")

    finally:
        print("Até mais")

cria_arquivo()
