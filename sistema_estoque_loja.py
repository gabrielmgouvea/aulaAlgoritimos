import os

def adicionar_produto(produtos):
    nome = input("Nome do produto: ")
    categoria = input("Categoria: ")
    
    while True:
        try:
            preco = float(input("Preço: "))
            if preco > 0:
                break
            else:
                print("O preço deve ser um número positivo.")
        except ValueError:
            print("Preço inválido. Por favor, insira um número válido.")

    while True:
        try:
            quantidade = int(input("Quantidade: "))
            if quantidade >= 0:
                break
            else:
                print("A quantidade não pode ser negativa.")
        except ValueError:
            print("Quantidade inválida. Por favor, insira um número inteiro.")

    produto = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
    produtos.append(produto)
    salvar_estoque(produtos)
    print("Produto adicionado com sucesso!")

def atualizar_quantidade(produtos):
    if not produtos:
        print("Nenhum produto registrado.")
        return

    nome_produto = input("Digite o nome do produto que deseja atualizar a quantidade: ")
    produto_encontrado = None
    
    for produto in produtos:
        if produto["nome"].lower() == nome_produto.lower():
            produto_encontrado = produto
            break
    
    if produto_encontrado:
        while True:
            try:
                quantidade_atualizada = int(input("Digite a nova quantidade (positiva para aumentar, negativa para reduzir): "))
                produto_encontrado["quantidade"] += quantidade_atualizada
                if produto_encontrado["quantidade"] < 0:
                    print("A quantidade não pode ser negativa!")
                    produto_encontrado["quantidade"] -= quantidade_atualizada
                else:
                    break
            except ValueError:
                print("Quantidade inválida. Por favor, insira um número inteiro.")
        
        salvar_estoque(produtos)
        print(f"Quantidade de {nome_produto} atualizada com sucesso!")
    else:
        print(f"Produto {nome_produto} não encontrado.")

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto registrado.")
    else:
        print("\nProdutos cadastrados:")
        for produto in produtos:
            print(f"Nome: {produto['nome']}, Categoria: {produto['categoria']}, Preço: R${produto['preco']:.2f}, Quantidade: {produto['quantidade']}")

def ordenar_produtos(produtos):
    if not produtos:
        print("Nenhum produto registrado.")
        return

    print("\nEscolha a opção de ordenação:")
    print("[1] Ordenar por preço")
    print("[2] Ordenar por quantidade")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        criterio = "preco"
    elif opcao == "2":
        criterio = "quantidade"
    else:
        print("Opção inválida.")
        return

    print("\nEscolha a ordem:")
    print("[1] Crescente")
    print("[2] Decrescente")
    ordem = input("Escolha uma opção: ")

    if ordem == "1":
        produtos.sort(key=lambda x: x[criterio])
    elif ordem == "2":
        produtos.sort(key=lambda x: x[criterio], reverse=True)
    else:
        print("Opção inválida.")
        return
    
    print(f"Produtos ordenados por {criterio}.")
    salvar_estoque(produtos)

def salvar_estoque(produtos):
    try:
        with open("estoque.txt", "w") as arquivo:
            for produto in produtos:
                arquivo.write(f"{produto['nome']},{produto['categoria']},{produto['preco']},{produto['quantidade']}\n")
        print("Os dados foram salvos no arquivo 'estoque.txt'.")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def carregar_estoque():
    produtos = []
    if os.path.exists("estoque.txt"):
        try:
            with open("estoque.txt", "r") as arquivo:
                for linha in arquivo:
                    dados = linha.strip().split(",")
                    if len(dados) == 4:
                        try:
                            produto = {
                                "nome": dados[0],
                                "categoria": dados[1],
                                "preco": float(dados[2]),
                                "quantidade": int(dados[3])
                            }
                            produtos.append(produto)
                        except ValueError:
                            print(f"Erro ao carregar o produto: {dados[0]} (dados inválidos).")
        except Exception as e:
            print(f"Erro ao carregar o arquivo: {e}")
    return produtos

def main():
    produtos = carregar_estoque()

    while True:
        print("Escolha uma opção:")
        print("[1] Adicionar produto")
        print("[2] Atualizar quantidade")
        print("[3] Listar produtos")
        print("[4] Ordenar produtos")
        print("[5] Salvar dados em arquivo")
        print("[6] Carregar dados do arquivo")
        print("[7] Sair")
        
        opcao = input("> ")

        if opcao == "1":
            adicionar_produto(produtos)
        elif opcao == "2":
            atualizar_quantidade(produtos)
        elif opcao == "3":
            listar_produtos(produtos)
        elif opcao == "4":
            ordenar_produtos(produtos)
        elif opcao == "5":
            salvar_estoque(produtos)
        elif opcao == "6":
            produtos = carregar_estoque()
        elif opcao == "7":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
