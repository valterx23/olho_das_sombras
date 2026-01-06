import subprocess
import os
def whois():
    os.system('clear')
    ip = input("Digite o endereço IP do alvo: ")
    comando = ["whois", ip]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)