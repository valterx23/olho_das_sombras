import subprocess
import os
def sfuzz():
    os.system('clear')
    ip = input("Digite o IP do alvo: ")
    porta = input("Digite a porta do respectivo serviço: ")
    wordlist = input("Digite o caminho da wordlist para atacar esse serviço: ")
    comando = ["sudo", "sfuzz", "-T", "-s", "-f", wordlist, "-S", ip, "-p", porta]
    resultado = subprocess.run(comando, text=True, capture_output=True)
    print("\n====== RESULTADO ======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO ======")
        print(resultado.stderr)