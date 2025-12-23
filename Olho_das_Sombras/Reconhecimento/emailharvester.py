import subprocess
import os
def emailharvester():
    os.system('clear')
    dominio = input("Digite o domínio alvo: ")
    engine = input("Digite o mecanismo de busca: ")
    comando = ["emailharvester", "-d", dominio, "-e", engine]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)