# Crie uma lista com 10 números inteiros aleatórios e escreva um programa para imprimir o
# maior e o menor número dessa lista.

# import random

# numeros = [random.randint(1,100) for i in range(10)]

# maior_numero = max(numeros)
# menor_numero = min(numeros)

# print(maior_numero, menor_numero)



# Escreva um programa que receba 5 nomes de frutas do usuário e os armazene em uma lista.
# Depois, peça ao usuário que informe uma fruta e verifique se ela está na lista.

# frutas = []

# for i in range(5):
#     fruta = input(f"Digite o numero da fruta {i+1}: ")
#     frutas.append(fruta)

# procurar_fruta = input("Qual fruta deseka procurar na lista? ")

# if procurar_fruta in frutas:
#     print(f"{procurar_fruta} está na lista de frutas")
# else:
#     print(f"{procurar_fruta} não está na lista de frutas")



# Crie uma lista de 10 elementos numéricos e escreva uma função que calcule a média dos
# números presentes na lista.

# numeros = []

# for i in range(10):
#     numero = int(input(f"Digite o numero {i+1} da lista de numeros: "))
#     numeros.append(numero)

# def media_lista(numeros):
#     soma = sum(numeros)
#     media = soma / len(numeros)
#     return media

# media = media_lista(numeros)
# print(f"A média da lista é de {media}")



# Crie uma lista de listas onde cada sublista deve conter três elementos: o nome de uma
# pessoa, sua idade e sua cidade. Imprima todas as informações no formato: "Nome: [Nome],
# Idade: [Idade], Cidade: [Cidade]".

# pessoas = [
#     ["Ana", 25, "São Paulo"],
#     ["João", 21, "Rio de Janeiro"],
#     ["Carlos", 32, "Curitiba"],
#     ["Fernanda", 31, "Belo Horizonte"],
#     ["Sérgio", 61, "Minas Gerais"]
# ]

# for pessoa in pessoas:
#     nome, idade, cidade = pessoa
#     print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")



# Escreva um programa que receba uma lista de números do usuário e remova todos os
# números duplicados, exibindo a lista resultante sem repetições.

# lista = []

# for i in range(5):
#     numero = int(input(f"Adicione um numero {i+1}: "))
#     if numero not in lista:
#         lista.append(numero)

# print(lista)

# Crie uma lista com 10 nomes de cidades escolhidas pelo usuário e escreva um programa para imprimir o 
# nome da cidade mais curta e a cidade mais longa (em número de caracteres).

# import random
# cidade = []

# for i in range(10):
#     cidades = input(f"Cidade {i+1}: ")
#     cidade.append(cidades)

# maior_cidade = max(cidade)
# menor_cidade = min(cidade)
# print(maior_cidade, menor_cidade)



# Escreva um programa que receba 5 nomes de países do usuário e os armazene em 
# uma lista. Depois, peça ao usuário que informe um país e verifique se ele está na lista.

# paises = []

# for i in range(5):
#     pais = input(f"Insira o nome de 5 países({i+1}): ")
#     paises.append(pais)

# procurar_pais = input("Qual país deseja saber se está na lista? ")

# if procurar_pais in paises:
#     print(f"O pais {procurar_pais}, está na lista de países")
# else:
#     print(f"O país {procurar_pais} não se encontra na lista.")


# Crie uma lista de 10 idades e escreva uma função que calcule
# a idade média das pessoas presentes na lista.

# idades = [10, 9, 8, 7, 6, 53, 42, 30, 22, 11]

# def media_idades():
#     soma = sum(idades)
#     media = soma / len(idades)
#     return media

# resultado = media_idades()
# print(resultado)

# Crie uma lista de listas onde cada sublista deve conter três elementos: 
# o nome de um livro, o nome do autor e o ano de publicação. Imprima todas 
# as informações no formato: "Livro: [Nome do Livro], Autor: [Nome do Autor], Ano: [Ano]".

# livros = [
#     ["Conto de Fadas", "João", 1998],
#     ["Terror", "Inacio", 2013],
#     ["Abobora", "Menisco", 1890],
#     ["Lambança", "Lionel", 1999]
# ]
# for livro in livros:
#     livro, autor, ano = livro
#     print(f"Livro: {livro}, Autor: {autor}, Ano: {ano}")


# Escreva um programa que receba uma lista de nomes de alunos do usuário e
# remova todos os nomes duplicados, exibindo a lista resultante sem repetições.

# nomes = []

# for nome in range(5):
#     n = input(f"Nome de numero {nome+1}: ")
#     if n not in nomes:
#         nomes.append(n)

# print(nomes)


# Crie um dicionário que armazene os dias da semana como chaves e o número de horas
# trabalhadas em cada dia como valores. Solicite ao usuário a entrada dessas horas e depois
# calcule o total de horas trabalhadas na semana.


# dias_semana = {
#     "Segunda-feira": 0,
#     "Terça-feira": 0,
#     "Quarta-feira": 0,
#     "Quinta-feira": 0,
#     "Sexta-feira": 0,
#     "Sábado": 0,
#     "Domingo": 0
# }

# for dia in dias_semana:
#     horas = int(input(f"Quantas horas você trabalhou na {dia}? "))
#     dias_semana[dia] = horas

# total_horas = sum(dias_semana.values())

# print(f"O total de horas trabalhadas na semana foi: {total_horas} horas.")


# Dada uma lista de nomes de alunos e suas respectivas notas em uma prova, crie um
# dicionário e permita que o usuário consulte e atualize a nota de um aluno específico.

# alunos_notas = {
#     "Ana": 8.5,
#     "Bruno": 7.0,
#     "Carla": 9.0,
#     "Diego": 6.5,
#     "Eduarda": 8.0
# }

# def consultar_nota(aluno):
#     if aluno in alunos_notas:
#         print(f"A nota de {aluno} é: {alunos_notas[aluno]}")
#     else:
#         print(f"Aluno {aluno} não encontrado.")

# def atualizar_nota(aluno, nova_nota):
#     if aluno in alunos_notas:
#         alunos_notas.update({aluno: nova_nota})
#         print(f"A nota de {aluno} foi atualizada para: {nova_nota}")
#     else:
#         print(f"Aluno {aluno} não encontrado.")

# while True:
#     print("1. Consultar nota")
#     print("2. Atualizar nota")
#     opcao = input("Escolha uma opção: ")

#     if opcao == "1":
#         nome_aluno = input("Digite o nome do aluno para consultar a nota: ")
#         consultar_nota(nome_aluno)

#     elif opcao == "2":
#         nome_aluno = input("Digite o nome do aluno para atualizar a nota: ")
#         nova_nota = float(input(f"Digite a nova nota de {nome_aluno}: "))
#         atualizar_nota(nome_aluno, nova_nota)
#     else:
#         print("Opção inválida. Tente novamente.")


# Crie um dicionário que armazene a quantidade de produtos em estoque em uma loja.
# Escreva uma função que verifique se um produto está em estoque e quantas unidades estão
# disponíveis.

# produtos = {
#     "Abacaxi": 10,
#     "Leite": 12,
#     "Pão": 30,
#     "Carne": 20
# }

# def verificar_produto():
#     verificar = input(f"Qual produto gostaria de verificar? ")
#     if verificar in produtos:
#         print(f"O produto {verificar} tem {produtos[verificar]} unidades em estoque.")
#     else:
#         print(f"O produto {verificar} não se encontra em nosso estoque.")

# verificar_produto()


# Crie duas listas: uma com nomes de países e outra com suas respectivas capitais. Converta
# essas duas listas em um dicionário, onde o país é a chave e a capital é o valor.

# paises = ["Brasil", "França", "Japão", "Alemanha", "Canadá"]
# capitais = ["Brasília", "Paris", "Tóquio", "Berlim", "Ottawa"]

# dicionario_paises_capitais = dict(zip(paises, capitais))

# print(dicionario_paises_capitais)



# Crie um dicionário para armazenar informações sobre estudantes, onde cada chave é o
# nome de um estudante e o valor é outro dicionário contendo suas notas nas disciplinas
# "Matemática", "Português" e "Ciências". Permita que o usuário acesse e altere as notas dos
# alunos.


# estudantes = {
#     "Alice": {"Matemática": 8, "Português": 7, "Ciências": 9},
#     "Bruno": {"Matemática": 6, "Português": 8, "Ciências": 7},
#     "Carla": {"Matemática": 9, "Português": 8, "Ciências": 10}
# }

# def acessar_alterar_notas():
#     aluno = input("Digite o nome do aluno: ")
#     if aluno in estudantes:
#         print(f"Notas de {aluno}: {estudantes[aluno]}")
        
#         alterar = input("Deseja alterar alguma nota? (s/n): ").lower()
#         if alterar == 's':
#             materia = input("Qual matéria deseja alterar? (Matemática, Português, Ciências): ")
#             # Verifica se a matéria existe para o aluno
#             if materia in estudantes[aluno]:
#                 nova_nota = float(input(f"Digite a nova nota de {materia}: "))
#                 # Atualiza a nota usando .update()
#                 estudantes[aluno].update({materia: nova_nota})
#                 print(f"Notas atualizadas de {aluno}: {estudantes[aluno]}")
#             else:
#                 print("Matéria não encontrada.")
#     else:
#         print("Aluno não encontrado.")

# acessar_alterar_notas()

# Escreva uma função que receba uma lista de números e retorne a soma de todos os
# números pares dessa lista.

# numeros = []
# def soma_pares():
#     for i in range(5):
#         numero = int(input(f"Digite os números da lista({i+1}/5): "))
#         if numero % 2 == 0:
#             numeros.append(numero)

#     soma = sum(numeros)
#     return soma       

# resultado = soma_pares()
# print(f"O resultado da soma dos numeros pares da lista {numeros}, é de {resultado}")

# Escreva uma função que receba um dicionário contendo nomes de produtos como chaves e
# seus preços como valores. A função deve retornar o nome do produto mais caro.

# def produto_mais_caro(produtos):
#     produto_caro = max(produtos.items(), key=lambda item: item[1])
#     return produto_caro[0]

# produtos = {
#     "Celular": 1500,
#     "Notebook": 3500,
#     "Tablet": 1200,
#     "Monitor": 800
# }

# resultado = produto_mais_caro(produtos)
# print(f"O produto mais caro é: {resultado}")


# Crie uma função que recebe uma lista e um número opcional. Se o número for fornecido, a
# função deve retornar a lista multiplicada por esse número. Se não for fornecido, a função deve
# retornar a lista original.

# numeros = [10, 8, 7, 6, 5]

# def multiplicar_lista():
#     numero_opcional = input("Insira um numero(OPICIONAL): ")
#     if numero_opcional == "":
#         print(f"{numeros}")
#         return None
#     else:
#         multiplicar = int(numero_opcional)
#         soma = sum(numeros)
#         mult = soma * multiplicar
#         return mult

# resultado = multiplicar_lista()

# if resultado is not None:
#     print(resultado)


# Escreva uma função que receba um dicionário representando um estoque de produtos
# (chave: nome do produto, valor: quantidade em estoque) e um produto vendido (nome do
# produto e quantidade vendida). A função deve atualizar o estoque conforme a venda e
# informar se a quantidade vendida excede o estoque disponível.

# def atualizar_estoque(estoque, produto_vendido, quantidade_vendida):
#     quantidade_estoque = estoque.get(produto_vendido, 0)
    
#     if quantidade_vendida > quantidade_estoque:
#         print(f"A quantidade vendida de {produto_vendido} excede o estoque disponível.")
#     else:
#         estoque[produto_vendido] = quantidade_estoque - quantidade_vendida
#         print(f"Venda realizada! Novo estoque de {produto_vendido}: {estoque[produto_vendido]}")

# estoque_produtos = {
#     "Celular": 10,
#     "Notebook": 5,
#     "Tablet": 8
# }

# produto = "Celular"
# quantidade = 3

# atualizar_estoque(estoque_produtos, produto, quantidade)


# Escreva uma função que recebe uma lista de dicionários, onde cada dicionário representa
# um estudante com seu nome e uma lista de notas. A função deve calcular a média de cada
# estudante e retornar um novo dicionário com os nomes dos estudantes como chaves e suas
# médias como valores.

# def calcular_medias(estudantes):
#     medias = {} 

#     for estudante in estudantes:
#         nome = estudante["nome"]
#         notas = estudante["notas"]
        
        
#         media = sum(notas) / len(notas) if notas else 0  
#         medias[nome] = media  

#     return medias


# lista_estudantes = [
#     {"nome": "Carlos", "notas": [8, 7.5, 9]},
#     {"nome": "Bruno", "notas": [6, 8, 7]},
#     {"nome": "João", "notas": [9, 9.5, 10]},
# ]

# resultado = calcular_medias(lista_estudantes)

# print(resultado)


# def buscaBinariaRecursiva(lista, chave, esquerda, direita):
#     if esquerda > direita:
#         return -1

#     meio = (esquerda + direita) // 2 

#     if lista[meio] == chave:
#         return meio
#     elif lista[meio] < chave:
#         return buscaBinariaRecursiva(lista, chave, meio + 1, direita)
#     else:
#         return buscaBinariaRecursiva(lista, chave, esquerda, meio - 1)


# chave = 15
# lista = [1, 5, 15, 20, 24, 45, 67, 76, 78, 100]

# pos = buscaBinariaRecursiva(lista, chave, 0, len(lista) - 1)

# if pos != -1:
#     print("Posição da chave", chave, "na lista:", pos)
# else:
#     print("A chave", chave, "não se encontra na lista")
