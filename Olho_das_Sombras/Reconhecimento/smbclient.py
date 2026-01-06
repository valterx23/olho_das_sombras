import subprocess
import os
def smbclient():
    os.system('clear')
    while True:
            print("""[1] Listar compartilhamentos
            [2] Acessar um compartilhamento
            [3] Listar arquivos dentro de um compartilhamento
            [4] Baixar arquivo
            [5] Enviar arquivo""")
            print("\nPressione Enter para sair....")
            escolha1 = input("\n> ").strip()

            if escolha1 == "1":
                print("Você tem usuário e senha? \n[1] Sim \n[2] Não")
                escolha = int(input("Digite sua escolha: "))
                if escolha == 1:
                    ip = input("Digite o ip do alvo: ")
                    user = input("Digite o usuário do alvo: ")
                    senha = input("Digite a senha: ")
                    comando = ["smbclient", "-L", f"//{ip}", "-U", f"{user}%{senha}"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
                elif escolha == 2:
                    ip = input("Digite o IP do alvo: ")
                    comando = ["smbclient", "-L", f"//{ip}", "-N"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
                else:
                    print("Digite uma opção válida")
            elif escolha1 == "2":
                print("Você tem usuário e senha? \n[1] Sim \n[2] Não")
                escolha = int(input("Digite sua escolha: "))

                if escolha == 1:
                    ip = input("Digite o ip do alvo: ")
                    user = input("Digite o usuário do alvo: ")
                    senha = input("Digite a senha: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-U", f"{user}%{senha}"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
                elif escolha == 2:
                    ip = input("Digite o IP do alvo: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-N"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
            elif escolha1 == "3":
                print("Você tem usuário e senha? \n[1] Sim \n[2] Não")
                escolha = int(input("Digite sua escolha: "))

                if escolha == 1:
                    ip = input("Digite o ip do alvo: ")
                    user = input("Digite o usuário do alvo: ")
                    senha = input("Digite a senha: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-c", "ls", "-U", f"{user}%{senha}"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
                elif escolha == 2:
                    ip = input("Digite o IP do alvo: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-c", "ls", "-N"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
            elif escolha1 == "4":
                print("Você tem usuário e senha? \n[1] Sim \n[2] Não")
                escolha = int(input("Digite sua escolha: "))

                if escolha == 1:
                    ip = input("Digite o ip do alvo: ")
                    user = input("Digite o usuário do alvo: ")
                    senha = input("Digite a senha: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    arq = input("Digite o nome do arquivo que você quer: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-c", f"get {arq}", "-U", f"{user}%{senha}"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
                elif escolha == 2:
                    ip = input("Digite o IP do alvo: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    arq = input("Digite o nome do arquivo: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-c", f"get {arq}", "-N"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
            elif escolha1 == "5":
                print("Você tem usuário e senha? \n[1] Sim \n[2] Não")
                escolha = int(input("Digite sua escolha: "))

                if escolha == 1:
                    ip = input("Digite o ip do alvo: ")
                    user = input("Digite o usuário do alvo: ")
                    senha = input("Digite a senha: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    arq = input("Digite o nome do arquivo que você quer: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-c", f"put {arq}", "-U", f"{user}%{senha}"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
                elif escolha == 2:
                    ip = input("Digite o IP do alvo: ")
                    share = input("Digite o compartilhamento que você quer: ")
                    arq = input("Digite o nome do arquivo: ")
                    comando = ["smbclient", f"//{ip}/{share}", "-c", f"put {arq}", "-N"]
                    resultado = subprocess.run(comando, capture_output=True, text=True)
                    print("\n====== RESULTADO ======")
                    print(resultado.stdout)

                    if resultado.stderr:
                        print("\n====== ERRO ======")
                        print(resultado.stderr)
            elif escolha1 == "":
                print("Saindo ....")
                break
            else:
                print("Digite uma opção válida")