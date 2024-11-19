import os

# Função para adicionar um aluno
def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    notas = []
    while len(notas) < 2 or len(notas) > 5:
        try:
            notas_input = input("Notas (separadas por vírgula): ").split(",")
            notas = [float(nota.strip()) for nota in notas_input]
            if len(notas) < 2 or len(notas) > 5:
                print("Por favor, insira entre 2 e 5 notas.")
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir números válidos.")
    
    # Verificar se todas as notas estão entre 0 e 10
    for i in range(len(notas)):
        while notas[i] < 0 or notas[i] > 10:
            try:
                notas[i] = float(input(f"Nota inválida {notas[i]}, insira uma nota entre 0 e 10: "))
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    media = sum(notas) / len(notas)
    aluno = {"nome": nome, "notas": notas, "media": media}
    alunos.append(aluno)

# Função para ordenar alunos por média usando Insertion Sort
def ordenar_alunos(alunos):
    for i in range(1, len(alunos)):
        chave = alunos[i]
        j = i - 1

        # Ordenação em ordem decrescente de média
        while j >= 0 and chave['media'] > alunos[j]['media']:
            alunos[j + 1] = alunos[j]
            j -= 1

        alunos[j + 1] = chave

# Função para salvar os dados em um arquivo
def salvar_em_arquivo(alunos):
    if os.path.exists("alunos.txt"):
        resposta = input("O arquivo 'alunos.txt' já existe. Deseja sobrescrevê-lo? (s/n): ").lower()
        if resposta != "s":
            print("Operação cancelada.")
            return
    
    try:
        with open("alunos.txt", "w") as arquivo:
            for aluno in alunos:
                arquivo.write(f"{aluno['nome']}, {aluno['media']:.2f}\n")
        print("Os dados foram salvos no arquivo 'alunos.txt'.")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

# Função para exibir os alunos ordenados
def exibir_alunos_ordenados(alunos):
    print("Alunos ordenados por média:")
    for aluno in alunos:
        print(f"{aluno['nome']} - Média: {aluno['media']:.2f}")

# Função principal
def main():
    alunos = []
    
    while True:
        adicionar_aluno(alunos)
        continuar = input("Deseja adicionar outro aluno? (s/n): ").lower()
        if continuar != "s":
            break
    
    ordenar_alunos(alunos)  # Ordenação usando Insertion Sort
    exibir_alunos_ordenados(alunos)
    salvar_em_arquivo(alunos)

# Execução do programa
if __name__ == "__main__":
    main()
