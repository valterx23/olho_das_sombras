import subprocess
import os
def reconhecimento_dns():
    os.system('clear')
    print(" [1] host\n [2] nslookup\n [3] dig ns")
    x1 = int(input("Digite a opção que você quer: "))
    if x1 == 1:
        dns = input("Digite o DNS do alvo: ")
        comando = ["host", dns]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif x1 == 2:
        dns = input("Digite o DNS do alvo: ")
        comando = ["nslookup", dns]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif x1 == 3:
        dns = input("Digite o DNS do alvo: ")
        comando = ["dig", "ns", dns]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)