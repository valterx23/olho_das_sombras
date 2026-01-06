import subprocess
import os
def openvas():
    os.system('clear')
    while True:
        print("[1] Iniciar OpenVas \n[2] Desligar OpenVAS")
        print("\nPressione Enter para sair....")
        escolha = input("> ").strip()
        if escolha == "1":
            print("Iniciando servidor OpenVAS")
            comando = ["gvm-start"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == "2":
            print("Desligando servidor OpenVas")
            comando = ["gvm-stop"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == "":
            print("Saindo do menu")
            break
        else:
            print("[!] Entrada inválida")