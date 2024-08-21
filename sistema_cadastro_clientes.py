import textwrap

def adicionar_cliente():
    adicionar_cliente = """
    [nu] Novo usuário
    [lc] Listar contas
    [q] Sair
    => """
    return input(textwrap.dedent(adicionar_cliente))

def criar_usuario(usuarios):
    nome = input("Informe o nome completo: ")
    email = input("Informe o seu e-mail: ")
    telefone = input("Informe o seu número de telefone: ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario = {"nome": nome, "email": email, "telefone": telefone, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")
    return usuario

def criar_conta(numero_conta, usuario):
    return {"numero_conta": numero_conta, "usuario": usuario}

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
        Nome:\t\t{conta['usuario']['nome']}
        Email:\t\t{conta['usuario']['email']}
        Telefone:\t{conta['usuario']['telefone']}
        Endereço:\t{conta['usuario']['endereco']}
        """
        print("=" * 50)
        print(textwrap.dedent(linha))

def main():

    usuarios = []
    contas = []

    while True:
        opcao = adicionar_cliente()

        if opcao == 'nu':
            usuario = criar_usuario(usuarios)
            numero_conta = len(contas) + 1
            conta = criar_conta(numero_conta, usuario)

            if conta:
                contas.append(conta)
                print("Conta criada com sucesso!")

        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            break

        else:
            print("Operação inválida")

main()