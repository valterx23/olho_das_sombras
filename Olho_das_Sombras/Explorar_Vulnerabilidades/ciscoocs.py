import subprocess
import os
def ciscoocs():
    os.system('clear')
    print("Essa aplicação utiliza intervalos de IP")
    ip1 = input("Digite o primeiro ip: ")
    ip2 = input("Digite o segundo ip: ")
    comando = ["cisco-ocs", ip1, ip2]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)