import subprocess
import os
def nmap():
    os.system('clear')
    print("Você quer: \n [1] Escaneamento TCP \n [2] Escaneamento UDP \n [3] Escaneamento Normal \n [4] Escaneamento com vuln TCP \n [5] Escaneamento com vuln UDP")
    escolha = int(input("Digite o número da sua escolha: "))
    if escolha == 1:
        ip = input("Digite o IP do alvo: ")
        vel = input("Digite entre 1-5 para determinar a velocidade: ")
        comando = ["nmap", "-sT", "-T", vel, ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif escolha == 2:
        print("Ok, você optou por um escaneamento mais demorado! Não se esqueça disso!")
        ip = input("Digite o IP do alvo: ")
        comando = ["nmap", "-sU", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif escolha == 3:
        print("Você quer fazer um escaneamento de todas as 65535 portas? [1] Sim [2] Não")
        rec_portas = int(input("Digite sua escolha: "))
        if rec_portas == 1:
            print("Esse tipo de escaneamento é mais demorado")
            ip = input("Digite o IP do alvo: ")
            comando = ["nmap", "-sV", "-p-", ip]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)

        elif rec_portas == 2:
            ip = input("Digite o IP do alvo: ")
            comando = ["nmap", "-sV", ip]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
    elif escolha == 4:
        print("Ok, você optou por um escaneamento mais demorado! Não se esqueça disso!")
        ip = input("Digite o IP do alvo: ")
        comando = ["nmap", "-sV", "--script", "vuln", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif escolha == 5:
        print("Ok, você optou por um escaneamento mais demorado! Não se esqueça disso!")
        ip = input("Digite o IP do alvo: ")
        comando = ["nmap", "-sU", "--script", "vuln", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Selecione uma opção correta!")