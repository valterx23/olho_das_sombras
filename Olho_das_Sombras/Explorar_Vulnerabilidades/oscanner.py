import subprocess
import os
def oscanner():
    os.system('clear')
    ip = input("Digite o ip do alvo: ")
    porta = input("Digite a porta do alvo: ")
    comando = ["oscanner", "-s", ip, "-P", porta]
    resultado = subprocess.run(comando, text=True, capture_output=True)
    print("\n====== RESULTADO ======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO ======")
        print(resultado.stderr)