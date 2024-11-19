import os

def adicionar_livro(livros):
    titulo = input("Título do livro: ")
    autor = input("Autor: ")

    while True:
        try:
            ano = int(input("Ano de publicação: "))
            if ano > 0:
                break
            else:
                print("Por favor, insira um ano válido (positivo).")
        except ValueError:
            print("Ano inválido. Por favor, insira um número inteiro.")

    while True:
        try:
            paginas = int(input("Número de páginas: "))
            if paginas > 0:
                break
            else:
                print("Por favor, insira um número válido de páginas (positivo).")
        except ValueError:
            print("Número de páginas inválido. Por favor, insira um número inteiro.")
    
    livro = {"titulo": titulo, "autor": autor, "ano": ano, "paginas": paginas}
    livros.append(livro)
    print("Livro adicionado com sucesso!")

def listar_livros(livros):
    if not livros:
        print("Nenhum livro registrado.")
    else:
        print("\nLivros cadastrados:")
        for livro in livros:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Páginas: {livro['paginas']}")

def insertion_sort(livros, criterio, ordem_crescente=True):
    for i in range(1, len(livros)):
        chave = livros[i]
        j = i - 1

        while j >= 0 and (
            (chave[criterio] < livros[j][criterio] if ordem_crescente else chave[criterio] > livros[j][criterio])
        ):
            livros[j + 1] = livros[j]
            j -= 1

        livros[j + 1] = chave

def ordenar_livros(livros):
    if not livros:
        print("Nenhum livro registrado.")
        return

    print("\nEscolha a opção de ordenação:")
    print("[1] Ordenar por ano de publicação")
    print("[2] Ordenar por número de páginas")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criterio = "ano"
    elif opcao == "2":
        criterio = "paginas"
    else:
        print("Opção inválida.")
        return

    print("\nEscolha a ordem:")
    print("[1] Crescente")
    print("[2] Decrescente")
    ordem = input("Escolha uma opção: ")

    if ordem == "1":
        ordem_crescente = True
    elif ordem == "2":
        ordem_crescente = False
    else:
        print("Opção inválida.")
        return

    insertion_sort(livros, criterio, ordem_crescente)
    print(f"Livros ordenados por {criterio}.")

def salvar_livros(livros):
    try:
        with open("biblioteca.txt", "w") as arquivo:
            for livro in livros:
                arquivo.write(f"{livro['titulo']},{livro['autor']},{livro['ano']},{livro['paginas']}\n")
        print("Os dados foram salvos no arquivo 'biblioteca.txt'.")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def carregar_livros():
    livros = []
    if os.path.exists("biblioteca.txt"):
        try:
            with open("biblioteca.txt", "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(",")
                    if len(dados) == 4:
                        try:
                            livro = {
                                "titulo": dados[0],
                                "autor": dados[1],
                                "ano": int(dados[2]),
                                "paginas": int(dados[3])
                            }
                            livros.append(livro)
                        except ValueError:
                            print(f"Erro ao carregar o livro: {dados[0]} (dados inválidos).")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
    return livros

def main():
    livros = carregar_livros()
    print("Bem-vindo à Biblioteca Digital!")

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar livro")
        print("2. Listar livros")
        print("3. Ordenar livros")
        print("4. Salvar dados em arquivo")
        print("5. Carregar dados do arquivo")
        print("6. Sair")
        
        opcao = input("> ")

        if opcao == "1":
            adicionar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            ordenar_livros(livros)
        elif opcao == "4":
            salvar_livros(livros)
        elif opcao == "5":
            livros = carregar_livros()
            print("Dados carregados com sucesso.")
        elif opcao == "6":
            salvar = input("Deseja salvar os dados antes de sair? (S/N): ").strip().lower()
            if salvar == "s":
                salvar_livros(livros)
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
