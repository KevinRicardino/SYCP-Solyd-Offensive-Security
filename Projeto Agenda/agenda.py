AGENDA = {}


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


def ler_detalhes_contato():
    telefone = input('>>>> Digite o nome do telefone: ')
    email = input('>>>> Digite o nome do email: ')
    endereco = input('>>>> Digite o nome do endereco: ')
    return telefone, email, endereco

def incluir_editar_contato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        'telefone': telefone,
        'email': email,
        'endereco': endereco,
    }
    salvar()
    print()
    print(f">>>> Contato '{contato}' adicionado/editado com sucesso.")


def excluir_contato(contato):
    try:
        AGENDA.pop(contato)
        salvar()
        print(f">>>> Contato '{contato}' excluído com sucesso.")
    except KeyError:
        print('>>>> Contato inexistente.')
    except Exception as error:
        print('>>>> Um erro inesperado ocorreu.')
        print(error)


def exportar_contatos(nome_do_arquivo):
    try:
        with open('database.csv', 'w') as arquivo:
            arquivo.write('nome,telefone,email,endereco\n')
            for contato in AGENDA:
                telefone = AGENDA[contato]['telefone']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                arquivo.write(f'{contato},{telefone},{email},{endereco}\n')
        print('>>>> Agenda exportada com sucesso.')
    except Exception as error:
        print('>>>> Algum erro ocorreu ao exportar contatos.')
        print(error)


def importar_contatos(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()[1:] # Pula o cabeçalho

            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado.')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu.')
        print(error)


def salvar():
    exportar_contatos('database.csv')


def carregar():
    try:
        with open('database.csv', 'r') as arquivo:
            linhas = arquivo.readlines()[1:] # Pula o cabeçalho
            for linha in linhas:
                detalhes = linha.strip().split(',')

                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                AGENDA[nome] = {
                    'telefone': telefone,
                    'email': email,
                    'endereco': endereco,
                }
        print('>>>> Database carregado com sucesso.')
        print(f'>>>> {len(AGENDA)} contatos carregados.')
    except FileNotFoundError:
        print('>>>> Arquivo não encontrado.')
    except Exception as error:
        print('>>>> Algum erro inesperado ocorreu.')
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
    print('\t[7] - Importar contatos CSV')
    print('\t[0] - Fechar agenda')
    print('='*50)
    print()


# INICIO DO PROGRAMA
carregar()
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
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == '4':
        contato = input('>>>> Digite o nome do contato: ')

        try:
            AGENDA[contato]
            print('>>>> Editando contato:', contato)
            telefone, email, endereco = ler_detalhes_contato()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print('>>>> Contato inexistente.')
    elif opcao == '5':
        contato = input('>>>> Digite o nome do contato: ')
        excluir_contato(contato)
    elif opcao == '6':
        nome_do_arquivo = input('Digite o nome do arquivo a ser exportado: ')
        exportar_contatos(nome_do_arquivo)
    elif opcao == '7':
        nome_do_arquivo = input('Digite o nome do arquivo a ser importado: ')
        print()
        importar_contatos(nome_do_arquivo)
    elif opcao == '0':
        print('>>>> Fechando programa...')
        break
    else:
        print('>>>> Opção inválida. Tente novamente: ')

    print()
    print('=' * 50)

    while True:
        continuar = input('\n>>>> Deseja continuar usando a agenda? (s/n): ').lower()

        if continuar == 's'.lower():
            break  # sai desse while e volta ao menu principal
        elif continuar == 'n'.lower():
            print('>>>> Encerrando agenda...')
            exit()  # encerra o programa
        else:
            print('>>>> Opção inválida. Digite apenas "s" ou "n": ')
