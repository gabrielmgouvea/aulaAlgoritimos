alunos_registrados = []

def menu():
    menu_texto = """
    [1] Cadastrar Alunos
    [2] Registrar Notas
    [3] Média da turma
    [4] Sair

    => """
    return input(menu_texto)

def cadastrar_alunos():
    nome = input("Qual o nome do aluno? ")
    aluno = {"nome": nome, "notas": []}
    alunos_registrados.append(aluno)
    print("Aluno cadastrado no Sistema!")

def registrar_notas():
    if not alunos_registrados:
        print("Nenhum aluno cadastrado ainda.")
        return

    nome = input("Qual o nome do aluno? ")
    for aluno in alunos_registrados:
        if aluno["nome"] == nome:
            try:
                nota = float(input("Digite a nota: "))
                aluno["notas"].append(nota)
                print("Nota registrada com sucesso!")
                return
            except ValueError:
                print("Nota inválida. Digite um número.")
                return
    print("Aluno não encontrado.")

def media_turma():
    if not alunos_registrados:
        print("Nenhum aluno cadastrado ainda.")
        return

    total_notas = 0
    quantidade_notas = 0

    for aluno in alunos_registrados:
        total_notas += sum(aluno["notas"])
        quantidade_notas += len(aluno["notas"])

    if quantidade_notas == 0:
        print("Nenhuma nota registrada ainda.")
    else:
        media = total_notas / quantidade_notas
        print(f"Média da turma: {media:.2f}")

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            cadastrar_alunos()
        elif opcao == "2":
            registrar_notas()
        elif opcao == "3":
            media_turma()
        elif opcao == "4":
            print("Sistema finalizado.")
            break
        else:
            print("Operação inválida.")

main()
