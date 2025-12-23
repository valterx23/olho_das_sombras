import subprocess
import os
def gobuster():
    os.system('clear')
    print("Qual é o tipo de escaneamento? [1] Diretórios [2] Subdomínios [3] S3")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        print("\nVocê quer procurar por arquivos específicos? [1] Sim [2] Não")
        x = int(input("Digite sua escolha: "))
        if x == 2:
            url = input("Digite sua URL: ")
            wordlist = input("Digite sua wordlist: ")
            comando = ["gobuster", "dir", "-u", url, "-w", wordlist]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif x == 1:
            url = input("Digite sua URL: ")
            wordlist = input("Digite sua wordlist: ")
            formato = input("Digite o formato dos arquivos (Digite os formatos entre vírgulas sem espaços): ")
            comando = ["gobuster", "dir", "-u", url, "-w", wordlist, "-x", formato]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        else:
            print("Digite uma opção válida")
    elif escolha == 2:
        dns = input("Digite o seu dns: ")
        wordlist = input("Digite o caminho da wordlist: ")
        comando = ["gobuster", "dns", "-d", dns, "-w", wordlist]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)

    elif escolha == 3:
        wordlist = input("Digite sua wordlist de S3 bucket: ")
        comando = ["gobuster", "s3", "-w", wordlist]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Digite uma opção válida")