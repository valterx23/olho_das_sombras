import subprocess
import os
def smbmap():
    os.system('clear')
    print("Você tem usuário e senha?\n [1] Sim\n [2] Não")
    escolha = int(input("Digite: "))
    if escolha == 1:
        usuario = input("Digite o usuário: ")
        senha = input("Digite a senha: ")
        ip = input("Digite o IP do alvo: ")
        comando = ["smbmap", "-u", usuario, "-p", senha, "-H", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)

    elif escolha == 2:
        ip = input("Digite o IP do alvo: ")
        comando = ["smbmap", "-H", ip, "-u", "''", "-p", "''" ]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Digite uma opção válida")