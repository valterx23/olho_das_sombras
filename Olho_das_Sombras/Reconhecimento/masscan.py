import subprocess
import os
def masscan():
    os.system('clear')
    portas = input("Digite um intervalo de portas(Deixando em branco as portas escaneadas serão de 1-1500): ")
    ip = input("Digite o IP do alvo: ")
    if portas == "":
        comando = ["masscan", "-sS", "--ports 1-1500", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        comando = ["masscan", "-sS", "--ports", portas, ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)