import subprocess
import os
def openvas():
    os.system('clear')
    while True:
        print("[1] Iniciar OpenVas \n[2] Desligar OpenVAS \n[0] Sair")
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            print("Iniciando servidor OpenVAS")
            comando = ["gvm-start"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == 2:
            print("Desligando servidor OpenVas")
            comando = ["gvm-stop"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == 0:
            print("Saindo do menu")
            break