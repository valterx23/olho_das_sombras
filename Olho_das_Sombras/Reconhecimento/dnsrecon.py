import subprocess
def dnsrecon():
    dns = input("Digite aqui o DNS do alvo:")
    wordlist = input("Digite o caminho da wordlist: ")
    comando = ["dnsrecon", "-d", dns, "-D", wordlist]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)