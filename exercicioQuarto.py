print('Olá! Eu sou Giovana Blank e este é o meu quarto programa em Python!')

lista_funcionarios = []
id_global = 4586926


def cadastrar_funcionario(id):
    global id_global
    nome = input('Digite o nome do funcionário: ').upper()
    setor = input('Digite o o setor do funcionário: ').upper()
    salario = float(input('Digite o salário do funcionário: '))
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    lista_funcionarios.append(funcionario.copy())
    print(f'Funcionário {nome} do setor {setor} cadastrado com sucesso!')

def consultar_funcionarios():
    while True:
        print('Você deseja: \n 1- Consultar todos os funcionários \n' \
    '2- Consultar funcionário por ID \n' \
        '3- Consultar funcionário por setor \n' \
            '4- Retornar ao menu')
        opcao = input(' ')

        if opcao not in ('1', '2', '3', '4'):
            print('Opção inválida. Tente novamente.')
            continue
        
        elif opcao == '1':
            for funcionario in lista_funcionarios:
                print(funcionario)
            
        elif opcao == '2':
            try:
                input_id = int(input('Digite o ID do funcionário: '))   
                encontrado = False
                for funcionario in lista_funcionarios:
                    if funcionario['id'] == input_id:
                        print(funcionario)
                        encontrado = True
                    if not encontrado:
                        print('Funcionário não encontrado.')
            except ValueError:
                print('ID inválido. Tente novamente.')

        elif opcao == '3':
            input_setor = input('Digite o setor do funcionário: ').upper()
            encontrados = [f for f in lista_funcionarios if f['setor'] == input_setor]
            if encontrados:
                for f in encontrados:
                    print(f)
            else: 
                print('Nenhum funcionário encontrado nesse setor.')
        elif opcao == '4':
            return
        else: 
            print('Opção inválida. Tente novamente.')
            
def remover_funcionario():
    while True:
        try:
            input_id = int(input('Digite o ID do funcionário a ser removido:'))
            for i, funcionario in enumerate(lista_funcionarios):
                if funcionario['id'] == input_id: 
                    removido = lista_funcionarios.pop(i)
                    print(f'Funcionário {removido["nome"]} removido com sucesso!'   )
                    return
            print('ID inválido.')
        except ValueError:
            print('Digite um ID válido.')

while True:
    print('MENU PRINCIPAL \n 1- Cadastrar funcionário \n 2- Consultar funcionários \n 3- Remover funcionário \n 4- Sair do programa')
    menu = input('Escolha uma opção: ')
    if menu == '1':
        id_global += 1
        cadastrar_funcionario(id_global)
    elif menu == '2':
        consultar_funcionarios()
    elif menu == '3': 
        remover_funcionario()
    elif menu == '4':
        print('Saindo do programa...')
        break
    else: 
        print('Opção inválida. Tente novamente.')