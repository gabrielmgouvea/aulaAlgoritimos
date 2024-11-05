alunos_registrados = []

def menu():
    menu = """
    [1] Cadastrar Alunos
    [2] Registrar Notas
    [3] Média da turma
    [4] Sair

    => """
    return input((menu))

def cadastar_alunos():
    nome = input(str("Qual o nome do aluno? "))
    
    alunos = {"nome": nome}
    alunos_registrados.append(alunos)
    print("Aluno cadastrado no Sistema!")
    return alunos

def registrar_notas(lista, chave):
    pos_ini = 0
    pos_fim = len(lista) - 1

    while pos_ini <= pos_fim:
        pos_meio = (pos_ini + pos_fim) // 2

        if lista[pos_meio] == chave:
            return pos_meio
        if lista[pos_meio] > chave:
            pos_fim = pos_meio - 1
        else:
            pos_ini = pos_meio + 1
    return -1

chave = input("Qual o nome do aluno?")
lista = alunos_registrados

pos = registrar_notas(lista, chave)
if pos != -1:
    print("Posição da chave", chave, "na lista:", pos)
else:
    print("A chave", chave, "não se encontra na lista")

def main():
    while True:
        opcao = menu()

        if opcao == "1":
            cadastar_alunos()
        elif opcao == "2":
            registrar_notas(lista, chave)
        elif opcao == "3":
            print("a")
        elif opcao == "4":
            print("Sistema finalizado.")
            break
        else:
            print("Operação invalida")

main()
