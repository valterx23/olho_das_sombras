import subprocess
import os
def medusa():
    os.system('clear')
    print("Você têm wordlist de usuario: [1] Sim [2] Não")
    escolha= int(input("Digite sua escolha: "))
    if escolha == 1:
        h = input("Digite o ip do alvo: ")
        u = input("Digite o caminho da sua wordlist de usuário: ")
        p = input("Digite o caminho da sua wordlist de senha:  ")
        m = input("Digite a numeração do protocolo a qual, você quer atacar: ")
        print("Você quer que o uso de Threads seja de 16 (padrão) \n [1] Sim \n [2] Não, prefiro colocar meu próprio valor")
        escolha2 = int(input("Digite sua escolha: "))
        if escolha2 == 1:
            comando = ["medusa", "-h", h, "-U", u, "-P", p, "-M", m, "-t", "16", "-v"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha2 == 2:
            threads = input("Digite o valor de Threads que você quer: ")
            comando = ["medusa", "-h", h, "-U", u, "-P", p, "-M", m, "-t", threads]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
    elif escolha == 2:
        h = input("Digite o ip do alvo: ")
        u = input("Digite o nome do usuário alvo: ")
        p = input("Digite o caminho da sua wordlist de senha:  ")
        m = input("Digite a numeração do protocolo a qual, você quer atacar: ")
        print(
            "Você quer que o uso de Threads seja de 16 (padrão) \n [1] Sim \n [2] Não, prefiro colocar meu próprio valor")
        escolha2 = int(input("Digite sua escolha: "))
        if escolha2 == 1:
            comando = ["medusa", "-h", h, "-u", u, "-P", p, "-M", m, "-t", "16"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha2 == 2:
            threads = input("Digite o valor de Threads que você quer: ")
            comando = ["medusa", "-h", h, "-u", u, "-P", p, "-M", m, "-t", threads]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)