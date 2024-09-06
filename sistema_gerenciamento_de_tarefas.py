import textwrap
lista_tarefa = []
def menu():
    menu = """
    [nt] Nova tarefa
    [vt] Visualizar tarefas
    [ft] Filtrar tarefa
    [q] Sair
    => """
    return input(textwrap.dedent(menu))

def adicionar_tarefa(nome, lista_tarefas, descricao, status, prioridade):
    descricao = input(str("Descrição da tarefa: "))
    status = input(str("Status da tarefa: 'pendente', 'em andamento' ou 'concluída': "))
    prioridade = input(str("Prioridade da tarefa: 'alta', 'média' ou 'baixa': "))

    tarefa = {"nome": nome, "descricao": descricao, "status": status, "prioridade": prioridade}
    lista_tarefas.append(tarefa)
    print(f"")
    return tarefa

def tarefa_criada(id, tarefa):
    return {"id": id, "tarefa": tarefa}

def visualizar_tarefas(tarefas):
    for tarefinha in tarefas:
        linha = f"""\
        id: {tarefinha['id']}
        descrição: {tarefinha['tarefa']['descricao']}
        status:\t{tarefinha['tarefa']["status"]}
        prioridade: {tarefinha['tarefa']['prioridade']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    nova_lista_filtrada = lista_tarefas
    status = input("Qual o status da tarefa? ")
    if status:
        nova_lista_filtrada = [lista_tarefas for lista_tarefas in nova_lista_filtrada if lista_tarefas["status"] == status]
    if status:
        nova_lista_filtrada = [lista_tarefas for tarefa in nova_lista_filtrada if lista_tarefas["prioridade"] == prioridade]
    return nova_lista_filtrada

def main():
    nome = []
    tarefas = []
    lista_tarefas = []
    descricao = []
    status = []
    prioridade = []

    while True:
        opcao = menu()

        if opcao == 'nt':
            tarefa = adicionar_tarefa(nome, lista_tarefas, descricao, status, prioridade)
            id = len(tarefas) + 1
            tarefinha = tarefa_criada(id, tarefa)

            if tarefinha:
                tarefas.append(tarefinha)
                print(f"Tarefa criada com sucesso! Id da tarefa: {id}")

        elif opcao == 'vt':
            visualizar_tarefas(tarefas)
        elif opcao == 'ft':
            filtrar_tarefas(lista_tarefas)

        elif opcao == 'q':
            break

        else:
            print("Operação inválida")

main()
