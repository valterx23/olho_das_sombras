import subprocess
import os
def enum4linux():
    os.system('clear')
    print("[1] Escaneamento Completo \n[2] Escaneamento null session \n[3] Escaneamento de usuários \n[4] Escaneamento de Grupos \n[5] Escaneamento de Shares \n[6] Escaneamento de domínio")
    scan = int(input("Digite sua escolha: "))
    if scan == 1:
        print("Esse escaneamento faz tudo que tem nessas opções acima")
        print("Você tem usuario e senha? [1] Sim [2] Não")
        credentials = int(input("Digite sua escolha: "))
        if credentials == 1:
            ip = input("Digite o IP do alvo: ")
            user = input("Digite o usuário: ")
            senha = input("Digite a senha: ")
            comando = ["enum4linux", "-a", "-u", user, "-p", senha, ip]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif credentials == 2:
            ip = input("Digite o IP do alvo: ")
            comando = ["enum4linux", "-a", ip]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
    elif scan == 2:
        print("Esse escaneamento tenta obter informações sem autenticação")
        ip = input("Digite o IP do alvo: ")
        comando = ["enum4linux", "-n", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif scan == 3:
        ip = input("Digite o IP do alvo: ")
        comando = ["enum4linux", "-U", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif scan == 4:
        ip = input("Digite o IP do alvo: ")
        comando = ["enum4linux", "-G", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif scan == 5:
        ip = input("Digite o IP do alvo: ")
        comando = ["enum4linux", "-S", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif scan == 6:
        ip = input("Digite o IP do alvo: ")
        comando = ["enum4linux", "-D", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Digite uma opção Válida")