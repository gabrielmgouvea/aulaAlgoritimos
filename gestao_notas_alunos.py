def adicionar_aluno(alunos):
    nome = input("Nome do aluno: ")
    notas = []
    while len(notas) < 2 or len(notas) > 5:
        notas = []
        while len(notas) < 2 or len(notas) > 5:
            try:
                notas_input = input("Notas (separadas por vírgula): ").split(",")
                notas = [float(nota.strip()) for nota in notas_input]
                if len(notas) < 2 or len(notas) > 5:
                    print("Por favor, insira entre 2 e 5 notas.")
            except ValueError:
                print("Entrada inválida. Certifique-se de inserir números válidos.")
    
    for i in range(len(notas)):
        while notas[i] < 0 or notas[i] > 10:
            try:
                notas[i] = float(input(f"Nota inválida {notas[i]}, insira uma nota entre 0 e 10: "))
            except ValueError:
                print("Entrada inválida. Tente novamente.")

    media = sum(notas) / len(notas)
    aluno = {"nome": nome, "notas": notas, "media": media}
    alunos.append(aluno)
    salvar_em_arquivo(alunos)

def adicionar_nota(alunos):
    nome = input("Nome do aluno: ")
    aluno_encontrado = False
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            aluno_encontrado = True
            while True:
                try:
                    nova_nota = float(input(f"Adicione uma nota para {nome}: "))
                    if 0 <= nova_nota <= 10:
                        aluno['notas'].append(nova_nota)
                        aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
                        print(f"Nota adicionada. Nova média de {nome}: {aluno['media']:.2f}")
                        break
                    else:
                        print("Nota deve ser entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Insira um número válido.")
            break

    if not aluno_encontrado:
        print("Aluno não encontrado.")
    
    salvar_em_arquivo(alunos)

def ordenar_alunos(alunos):
    alunos.sort(key=lambda x: x['media'], reverse=True)

def salvar_em_arquivo(alunos):
    try:
        with open("alunos.txt", "w") as arquivo:
            for aluno in alunos:
                arquivo.write(f"{aluno['nome']}, {aluno['media']:.2f}\n")
        print("Os dados foram salvos no arquivo 'alunos.txt'.")
    except Exception as e:
        print(f"Erro ao salvar os dados no arquivo: {e}")

def exibir_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        print("Alunos com suas notas e média:")
        for aluno in alunos:
            notas_str = ", ".join([str(nota) for nota in aluno['notas']])
            print(f"{aluno['nome']} - Notas: {notas_str} - Média: {aluno['media']:.2f}")

def main():
    alunos = []
    while True:
        print("\nMenu:")
        print("[1] Adicionar Aluno")
        print("[2] Adicionar Nota")
        print("[3] Ordenar Alunos por Média")
        print("[4] Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_aluno(alunos)
        elif opcao == '2':
            adicionar_nota(alunos)
        elif opcao == '3':
            ordenar_alunos(alunos)
            print("Alunos ordenados por média.")
        elif opcao == '4':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
