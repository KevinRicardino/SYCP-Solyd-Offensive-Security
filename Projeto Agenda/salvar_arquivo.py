"""
'r'  - Abre para leitura (arquivo deve existir)
'w'  - Abre para escrita (sobrescreve o arquivo)
'a'  - Abre para escrita (adiciona conteúdo ao final)
'+'  - Permite leitura e escrita no mesmo arquivo
'b'  - Abre o arquivo em modo binário (bytes)
"""

try:
    with open('nomes.txt', 'a') as arquivo:
        arquivo.write('kevin\n')
except Exception as error:
    print('Algum erro ocorreu.')
    print(error)

