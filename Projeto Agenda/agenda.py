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
    for contato in AGENDA:
        buscar_contato(contato)
        print('----------------------')


def buscar_contato(contato):
    print('Nome:', contato)
    print('Telefone:', AGENDA[contato]['telefone'])
    print('Email:', AGENDA[contato]['email'])
    print('Endereco:', AGENDA[contato]['endereco'])



def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    print(f">>>> Contato '{contato}' adicionado/editado com sucesso.")


def excluir_contato(contato):
    AGENDA.pop(contato)
    print(f">>>> Contato{contato} excluido com sucesso.")


def imprimir_menu():
    print()
    print(' AGENDA '.center(50, '='))
    print('\t[1] - Mostrar todos os contatos da agenda')
    print('\t[2] - Buscar contato')
    print('\t[3] - Incluir contato')
    print('\t[4] - Editar contato')
    print('\t[5] - Excluir contato')
    print('\t[0] - Fechar agenda')
    print('='*50)
    print()

imprimir_menu()

opcao = input('>>> Escolha uma opção: ')
if opcao == '1':
    mostrar_contatos()
elif opcao == '2':
    contato = input('>>> Digite o nome do contato: ')
    buscar_contato(contato)
elif opcao == '3':
    contato = input('>>> Digite o nome do contato: ')
    telefone = input('>>> Digite o nome do telefone: ')
    email = input('>>> Digite o nome do email: ')
    endereco = input('>>> Digite o nome do endereco: ')
    incluir_editar_contato(contato, telefone, email, endereco)
elif opcao == '5':
    contato = input('>>> Digite o nome do contato: ')
    excluir_contato(contato)
elif opcao == '0':
    print('>>> Fechando programa...')
else:
    print('>>> Opção inválida. Tente novamente: ')