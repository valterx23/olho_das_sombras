import subprocess
import os
def cat():
    os.system('clear')
    print("Você tem wordlist de usuario e senha? \n [1] Sim \n [2] Não")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        ip = input("Digite o ip do alvo: ")
        usuario = input("Digite o caminho da wordlist de usuário: ")
        senha = input("Digite o caminho da wordlist de senha: ")
        comando = ["CAT", "-w", usuario, "-a", senha, "-h", ip]
        resultado = subprocess.run(comando, text=True, capture_output=True)
        print("\n====== RESULTADO ======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO ======")
            print(resultado.stderr)
    elif escolha == 2:
        ip = input("Digite o ip do alvo: ")
        porta = input("Digite uma porta: ")
        comando = ["CAT", "-h", ip, "-p", porta]
        resultado = subprocess.run(comando, text=True, capture_output=True)
        print("\n====== RESULTADO ======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO ======")
            print(resultado.stderr)
    else:
        print("[!] Opção inválida")