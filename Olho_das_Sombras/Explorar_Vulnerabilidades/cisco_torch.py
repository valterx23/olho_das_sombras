import subprocess
import os
def cisco_torch():
    os.system('clear')
    ip = input("Digite o ip do alvo: ")
    comando = ["cisco-torch", "-t", "-s", "-w", ip]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)