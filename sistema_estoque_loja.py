import os

estoque = []

def adicionar_produto():
    try:
        nome = input("Nome do produto: ")
        categoria = input("Categoria: ")
        preco = float(input("Preço: "))
        if preco <= 0:
            raise ValueError("O preço deve ser positivo.")
        quantidade = int(input("Quantidade: "))
        if quantidade < 0:
            raise ValueError("A quantidade deve ser um número inteiro não negativo.")
        produto = {"nome": nome, "categoria": categoria, "preco": preco, "quantidade": quantidade}
        estoque.append(produto)
        print("Produto adicionado com sucesso!")
    except ValueError as e:
        print(f"Erro: {e}")

def atualizar_quantidade():
    nome = input("Digite o nome do produto que deseja atualizar: ")
    for produto in estoque:
        if produto["nome"].lower() == nome.lower():
            try:
                nova_quantidade = int(input("Nova quantidade (use valores negativos para reduzir): "))
                if produto["quantidade"] + nova_quantidade < 0:
                    raise ValueError("A quantidade final não pode ser negativa.")
                produto["quantidade"] += nova_quantidade
                print("Quantidade atualizada com sucesso!")
                return
            except ValueError as e:
                print(f"Erro: {e}")
                return
    print("Produto não encontrado.")

def listar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    print("\nProdutos no estoque:")
    for produto in estoque:
        print(f"{produto['nome']} - {produto['categoria']} - R$ {produto['preco']:.2f} - {produto['quantidade']} unidades")
    print()

def insertion_sort(lista, chave, ordem_crescente=True):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and (
            (lista[j][chave] > atual[chave] if ordem_crescente else lista[j][chave] < atual[chave])
        ):
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = atual

def ordenar_produtos():
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    print("\nEscolha uma opção para ordenar:")
    print("[1] Ordenar por preço")
    print("[2] Ordenar por quantidade")
    opcao = input("> ")
    if opcao not in ["1", "2"]:
        print("Opção inválida.")
        return
    chave = "preco" if opcao == "1" else "quantidade"
    ordem = input("Ordenar em ordem crescente? (S/N): ").lower()
    ordem_crescente = ordem == "s"
    insertion_sort(estoque, chave, ordem_crescente)
    print(f"Produtos ordenados por {chave} com sucesso!")

def salvar_estoque():
    try:
        with open("estoque.txt", "w") as arquivo:
            for produto in estoque:
                linha = f"{produto['nome']},{produto['categoria']},{produto['preco']:.2f},{produto['quantidade']}\n"
                arquivo.write(linha)
        print("Dados salvos com sucesso no arquivo 'estoque.txt'.")
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")

def carregar_estoque():
    if not os.path.exists("estoque.txt"):
        print("Arquivo 'estoque.txt' não encontrado.")
        return
    try:
        with open("estoque.txt", "r") as arquivo:
            for linha in arquivo:
                nome, categoria, preco, quantidade = linha.strip().split(",")
                estoque.append({
                    "nome": nome,
                    "categoria": categoria,
                    "preco": float(preco),
                    "quantidade": int(quantidade)
                })
        print("Dados carregados com sucesso do arquivo 'estoque.txt'.")
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}")

def menu():
    while True:
        print("\nBem-vindo ao Sistema de Gestão de Estoque!")
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
            adicionar_produto()
        elif opcao == "2":
            atualizar_quantidade()
        elif opcao == "3":
            listar_produtos()
        elif opcao == "4":
            ordenar_produtos()
        elif opcao == "5":
            salvar_estoque()
        elif opcao == "6":
            carregar_estoque()
        elif opcao == "7":
            salvar_antes = input("Deseja salvar os dados antes de sair? (S/N): ").lower()
            if salvar_antes == "s":
                salvar_estoque()
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

menu()
