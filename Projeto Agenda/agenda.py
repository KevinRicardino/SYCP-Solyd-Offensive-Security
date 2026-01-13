AGENDA = {}

AGENDA['guilherme'] = {
    'telefone': '999928272',
    'email': 'guilherme@solyd.com.br',
    'endereco': 'Av. 1',
}

AGENDA['maria'] = {
    'telefone': '999282727',
    'email': 'maria@solyd.com.br',
    'endereco': 'Av. 2',
}

def mostrar_contatos():
    if AGENDA:
        print()
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('>>>> Agenda vazia.')


def buscar_contato(contato):
    try:
        print()
        print('\t----------------------')
        print('\tNome:', contato)
        print('\tTelefone:', AGENDA[contato]['telefone'])
        print('\tEmail:', AGENDA[contato]['email'])
        print('\tEndereco:', AGENDA[contato]['endereco'])
        print('\t----------------------')
    except KeyError:
        print('\t>>>> Contato inexistente.')
    except Exception as error:
        print('\t>>>> Um erro inesperado ocorreu.')
        print(error)


def incluir_editar_contato(contato):
    telefone = input('>>>> Digite o nome do telefone: ')
    email = input('>>>> Digite o nome do email: ')
    endereco = input('>>>> Digite o nome do endereco: ')

    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print()
    print(f">>>> Contato '{contato}' adicionado/editado com sucesso.")


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        print(f">>>> Contato '{contato}' excluído com sucesso.")
    except KeyError:
        print('>>>> Contato inexistente.')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu.')
        print(error)


def exportar_contatos():
    try:
        with open('agenda.csv', 'w') as arquivo:
            arquivo.write('nome;telefone;email;endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato};{telefone};{email};{endereco}\n')
        print('>>>> Agenda exportada com sucesso.')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos.')
        print(error)


def imprimir_menu():
    print()
    print(' AGENDA '.center(50, '='))
    print('\t[1] - Mostrar todos os contatos da agenda')
    print('\t[2] - Buscar contato')
    print('\t[3] - Incluir contato')
    print('\t[4] - Editar contato')
    print('\t[5] - Excluir contato')
    print('\t[6] - Exportar contatos para CSV')
    print('\t[0] - Fechar agenda')
    print('='*50)
    print()


while True:
    imprimir_menu()

    opcao = input('>>>> Escolha uma opção: ')
    if opcao == '1':
        mostrar_contatos()
    elif opcao == '2':
        contato = input('>>>> Digite o nome do contato: ')
        buscar_contato(contato)
    elif opcao == '3':
        contato = input('>>>> Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>> Contato já existente.')
        except KeyError:
            incluir_editar_contato(contato)
    elif opcao == '4':
        contato = input('>>>> Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>> Editando contato:', contato)
            incluir_editar_contato(contato)
        except KeyError:
            print('>>>> Contato inexistente.')
    elif opcao == '5':
        contato = input('>>>> Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        exportar_contatos()
    elif opcao == '0':
        print('>>>> Fechando programa...')
        break
    else:
        print('>>>> Opção inválida. Tente novamente: ')

    print()
    print('=' * 50)
    continuar = input('\n>>>> Deseja continuar usando a agenda? (s/n): ').lower()
    if continuar != 's':
        print('>>>> Encerrando agenda...')
        break
