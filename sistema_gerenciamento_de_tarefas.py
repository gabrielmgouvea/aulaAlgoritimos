import textwrap

lista_tarefas = []

def menu():
    menu = """
    [nt] Nova tarefa
    [vt] Visualizar tarefas
    [ft] Filtrar tarefa
    [q] Sair
    => """
    return input(textwrap.dedent(menu))


def adicionar_tarefa(lista_tarefas):
    descricao = input(str("Descrição da tarefa: "))
    status = input(str("Status da tarefa ('pendente', 'em andamento', 'concluída'): "))
    prioridade = input(str("Prioridade da tarefa ('alta', 'média', 'baixa'): "))

    tarefa = {"descricao": descricao, "status": status, "prioridade": prioridade}
    lista_tarefas.append(tarefa)
    return tarefa

def tarefa_criada(id, tarefa):
    return {"id": id, "tarefa": tarefa}

def visualizar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas cadastradas.")
    for tarefinha in tarefas:
        linha = f"""\
        id: {tarefinha['id']}
        Descrição: {tarefinha['tarefa']['descricao']}
        Status: {tarefinha['tarefa']["status"]}
        Prioridade: {tarefinha['tarefa']['prioridade']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

def filtrar_tarefas(lista_tarefas, status=None, prioridade=None):
    nova_lista_filtrada = lista_tarefas

    status = input("Status(pendente, em andamento, concluída): ").strip()
    prioridade = input("Prioridade(alta, média, baixa): ").strip()
    
    if status:
        nova_lista_filtrada = [tarefa for tarefa in nova_lista_filtrada if tarefa["status"] == status]
    
    if prioridade:
        nova_lista_filtrada = [tarefa for tarefa in nova_lista_filtrada if tarefa["prioridade"] == prioridade]

    if not nova_lista_filtrada:
        print("Nenhuma tarefa encontrada com os critérios fornecidos.")
    else:
        visualizar_tarefas([{"id": idx + 1, "tarefa": tarefa} for idx, tarefa in enumerate(nova_lista_filtrada)])

    return nova_lista_filtrada

def main():
    tarefas = []

    while True:
        opcao = menu()

        if opcao == 'nt':
            tarefa = adicionar_tarefa(lista_tarefas)
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
            print("Saindo do sistema...")
            break

        else:
            print("Operação inválida, tente novamente.")

main()
