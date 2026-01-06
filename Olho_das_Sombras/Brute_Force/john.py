import subprocess
import os
def john():
    os.system('clear')
    print("Você tem um arquivo hash compátivel com o John? \n [1] SIM  \n [2] NÃO")
    v = int(input("Digite sua escolha: "))
    if v == 1:
        wordlist = input("Digite o caminho da sua wordlist: ")
        arq_hash = input("Digite o caminho do arquivo .hash: ")
        comando = ["john", f"--wordlist={wordlist}", arq_hash]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)

    elif v == 2:
        arquivo_zip = input("Digite o caminho do arquivo zip: ")
        local = input("Caminho de destino para o arquivo .hash: ")
        comando = ["zip2john", arquivo_zip, ">", local]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Digite uma opção válida")