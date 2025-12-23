import subprocess
import os
def amap():
    os.system('clear')
    ip = input("Digite o IP do alvo: ")
    porta = int(input("Digite o número da porta: "))
    comando = ["amap", ip, str(porta)]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)