import os
import subprocess
def the_harvester():
    os.system('clear')
    dominio = input("Digite o domínio alvo: ")

    providers = ['duckduckgo', 'bing', 'baidu', 'dnsdumpster', 'hunter', 'sitedossier']

    for provider in providers:
        print(f"\n[+] Rodando TheHarvester com fonte: {provider}...")
        comando = ["theHarvester", "-d", dominio, "-b", provider]
        resultado = subprocess.run(comando, text=True, capture_output=True)
        print("\n====== RESULTADO ======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO ======")
            print(resultado.stderr)