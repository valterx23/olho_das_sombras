import subprocess
def gobuster():
    print("Você quer encontrar um formato de arquivo específico? \n[1] Sim \n[2] Não")
    escolha = int(input("Digite sua escolha: "))
    if escolha == 1:
        dns = input("Digite o DNS do alvo(com http): ")
        wordlist = input("Digite o caminho da wordlist que será utilizada: ")
        print("Se você quiser mais de um arquivo tem que digitar assim: ex1,ex2,ex3")
        arq_esp = input("Digite o(os) arquivo(os) especifico(os): ")
        comando = ["gobuster", "dir", "-u", dns, "-w", wordlist, "-x", arq_esp]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif escolha == 2:
        dns = input("Digite o DNS do alvo(com http): ")
        wordlist = input("Digite o caminho da wordlist que será utilizada: ")
        comando = ["gobuster", "dir", "-u", dns, "-w", wordlist]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Digite uma opção válida")