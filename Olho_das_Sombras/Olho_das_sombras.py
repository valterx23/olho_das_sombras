<<<<<<< HEAD
# == BIBLIOTECA PARA INICIALIZAR O MENU
from Menu.menu import iniciar_menu

# == INICIALIZAÇÃO ==
if __name__ == "__main__":
    iniciar_menu()
=======
# ================= BIBLIOTECAS ===================
from art import *
import subprocess
import random
# ================= FUNÇÕES =================
# == RECONHECIMENTO ==
def the_harvester():
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
def emailharvester():
    dominio = input("Digite o domínio alvo: ")
    engine = input("Digite o mecanismo de busca: ")
    comando = ["emailharvester", "-d", dominio, "-e", engine]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)
def reconhecimento_dns():
    print(" [1] host\n [2] nslookup\n [3] dig ns")
    x1 = int(input("Digite a opção que você quer: "))
    if x1 == 1:
        dns = input("Digite o DNS do alvo: ")
        comando = ["host", dns]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif x1 == 2:
        dns = input("Digite o DNS do alvo: ")
        comando = ["nslookup", dns]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    elif x1 == 3:
        dns = input("Digite o DNS do alvo: ")
        comando = ["dig", "ns", dns]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
def whois():
    ip = input("Digite o endereço IP do alvo: ")
    comando = ["whois", ip]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)
def nmap():
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
        rec_portas = int(input("Você quer fazer um escaneamento de todas as 65535 portas? [1] Sim [2] Não"))
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
def masscan():
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
def amap():
    ip = input("Digite o IP do alvo: ")
    porta = int(input("Digite o número da porta: "))
    comando = ["amap", ip, str(porta)]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)
def smbmap():
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
        comando = ["smbmap", "-H", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
    else:
        print("Digite uma opção válida")
def enum4linux():
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

# == EXPLORAR VULNERABILIDADES ==
def cat():
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
        print("Digite uma Opção Válida")
def cisco_torch():
    ip = input("Digite o ip do alvo: ")
    comando = ["cisco-torch", "-t", "-s", "-w", ip]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)
def cgepl():
    ip = input("Digite o IP do roteador alvo: ")
    opcoes = r'''[1] - Cisco 677/678 Telnet Buffer Overflow Vulnerability
[2] - Cisco IOS Router Denial of Service Vulnerability
[3] - Cisco IOS HTTP Auth Vulnerability
[4] - Cisco IOS HTTP Configuration Arbitrary Administrative Access Vulnerability
[5] - Cisco Catalyst SSH Protocol Mismatch Denial of Service Vulnerability
[6] - Cisco 675 Web Administration Denial of Service Vulnerability
[7] - Cisco Catalyst 3500 XL Remote Arbitrary Command Vulnerability
[8] - Cisco IOS Software HTTP Request Denial of Service Vulnerability
[9] - Cisco 514 UDP Flood Denial of Service Vulnerability
[10] - CiscoSecure ACS for Windows NT Server Denial of Service Vulnerability
[11] - Cisco Catalyst Memory Leak Vulnerability
[12] - Cisco CatOS CiscoView HTTP Server Buffer Overflow Vulnerability
[13] - 0 Encoding IDS Bypass Vulnerability (UTF)
[14] - Cisco IOS HTTP Denial of Service Vulnerability
'''
    print(opcoes)
    vuln = input("Digite qual vulnerabilidade você quer explorar: ")
    comando = ["perl", "cge.pl", ip, vuln]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)
def ciscoocs():
    print("Essa aplicação utiliza intervalos de IP")
    ip1 = input("Digite o primeiro ip: ")
    ip2 = input("Digite o segundo ip: ")
    comando = ["cisco-ocs", ip1, ip2]
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print("\n====== RESULTADO =======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO =======")
        print(resultado.stderr)
def oscanner():
    ip = input("Digite o ip do alvo: ")
    porta = input("Digite a porta do alvo: ")
    comando = ["oscanner", "-s", ip, "-P", porta]
    resultado = subprocess.run(comando, text=True, capture_output=True)
    print("\n====== RESULTADO ======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO ======")
        print(resultado.stderr)
def sfuzz():
    ip = input("Digite o IP do alvo: ")
    porta = input("Digite a porta do respectivo serviço: ")
    wordlist = input("Digite o caminho da wordlist para atacar esse serviço: ")
    comando = ["sudo", "sfuzz", "-T", "-s", "-f", wordlist, "-S", ip, "-p", porta]
    resultado = subprocess.run(comando, text=True, capture_output=True)
    print("\n====== RESULTADO ======")
    print(resultado.stdout)

    if resultado.stderr:
        print("\n====== ERRO ======")
        print(resultado.stderr)
def exploitdb():
    while True:
        print(" [1] Procurar exploit \n [2] Baixar exploit \n [0] Voltar ao início")
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            busca = input("Digite o que você quer buscar: ")
            comando = ["searchsploit", busca]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == 2:
            xploit = input("Digite a numeração do exploit: ")
            comando1 = ["cd", "/dados/Exploits"]
            resultado1 = subprocess.run(comando1)
            print(resultado1)
            comando = ["searchsploit", "-m", xploit]
            resultado = subprocess.run(comando, text=True, capture_output=True)
            print("\n====== RESULTADO ======")
            print(resultado.stdout)


            if resultado.stderr:
                print("\n====== ERRO ======")
                print(resultado.stderr)

        elif escolha == 0:
            break
        else:
            print("Digite uma opção Válida")
def openvas():
    while True:
        print("[1] Iniciar OpenVas \n[2] Desligar OpenVAS \n[0] Sair")
        escolha = int(input("Digite sua escolha: "))
        if escolha == 1:
            print("Iniciando servidor OpenVAS")
            comando = ["gvm-start"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == 2:
            print("Desligando servidor OpenVas")
            comando = ["gvm-stop"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha == 0:
            print("Saindo do menu")
            break

# == BRUTE FORCE ==
def john():
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
def medusa():
    print("Você têm wordlist de usuario: [1] Sim [2] Não")
    escolha= int(input("Digite sua escolha: "))
    if escolha == 1:
        h = input("Digite o ip do alvo: ")
        u = input("Digite o caminho da sua wordlist de usuário: ")
        p = input("Digite o caminho da sua wordlist de senha:  ")
        m = input("Digite a numeração do protocolo a qual, você quer atacar: ")
        print("Você quer que o uso de Threads seja de 16 (padrão) \n [1] Sim \n [2] Não, prefiro colocar meu próprio valor")
        escolha2 = int(input("Digite sua escolha: "))
        if escolha2 == 1:
            comando = ["medusa", "-h", h, "-U", u, "-P", p, "-M", m, "-t", "16", "-v"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha2 == 2:
            threads = input("Digite o valor de Threads que você quer: ")
            comando = ["medusa", "-h", h, "-U", u, "-P", p, "-M", m, "-t", threads]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
    elif escolha == 2:
        h = input("Digite o ip do alvo: ")
        u = input("Digite o nome do usuário alvo: ")
        p = input("Digite o caminho da sua wordlist de senha:  ")
        m = input("Digite a numeração do protocolo a qual, você quer atacar: ")
        print(
            "Você quer que o uso de Threads seja de 16 (padrão) \n [1] Sim \n [2] Não, prefiro colocar meu próprio valor")
        escolha2 = int(input("Digite sua escolha: "))
        if escolha2 == 1:
            comando = ["medusa", "-h", h, "-u", u, "-P", p, "-M", m, "-t", "16"]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
        elif escolha2 == 2:
            threads = input("Digite o valor de Threads que você quer: ")
            comando = ["medusa", "-h", h, "-u", u, "-P", p, "-M", m, "-t", threads]
            resultado = subprocess.run(comando, capture_output=True, text=True)
            print("\n====== RESULTADO =======")
            print(resultado.stdout)

            if resultado.stderr:
                print("\n====== ERRO =======")
                print(resultado.stderr)
# == Estética ==
def frases_hacking():
    frases = ["Hack the planet.",
        "Trust no input, verify everything.",
        "In packets we trust.",
        "Social engineering beats encryption.",
        "The quieter you become, the more you are able to hear.",
        "Buffer overflow: because size matters.",
        "Real hackers don't brute force, they think.",
        "Cybersecurity is not a product, it's a process.",
        "Hackers don't break in, they log in.",
        "Knowledge is power. And power corrupts."]
    return random.choice(frases)
# =========== LOGO =======================
tprint("OLHO DAS SOMBRAS", font="standard")
logo = r'''
          ⢀⣀⣤⣤⣤⣤⣴⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⠿⠛⠋⠉⠁⠀⠀⠀⠈⠙⠻⢷⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣤⣾⡿⠋⠁⠀⣠⣶⣿⡿⢿⣷⣦⡀⠀⠀⠀⠙⠿⣦⣀⠀⠀⠀⠀
⠀⠀⢀⣴⣿⡿⠋⠀⠀⢀⣼⣿⣿⣿⣶⣿⣾⣽⣿⡆⠀⠀⠀⠀⢻⣿⣷⣶⣄⠀
⠀⣴⣿⣿⠋⠀⠀⠀⠀⠸⣿⣿⣿⣿⣯⣿⣿⣿⣿⣿⠀⠀⠀⠐⡄⡌⢻⣿⣿⡷
⢸⣿⣿⠃⢂⡋⠄⠀⠀⠀⢿⣿⣿⣿⣿⣿⣯⣿⣿⠏⠀⠀⠀⠀⢦⣷⣿⠿⠛⠁
⠀⠙⠿⢾⣤⡈⠙⠂⢤⢀⠀⠙⠿⢿⣿⣿⡿⠟⠁⠀⣀⣀⣤⣶⠟⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠿⣾⣠⣆⣅⣀⣠⣄⣤⣴⣶⣾⣽⢿⠿⠟⠋⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠙⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            '''
print(logo)
print(f"{frases_hacking()}")
# =============== ESCOLHA DO QUAL TIPO DE SCRIPT =====================
while True:
    print("")
    print("\nO que você quer hoje?")
    print("\n[1] Reconhecimento \n[2] Explorar Vulnerabilidades \n[3] Brute Force \n[0] Sair do Programa")
    ferramenta = int(input("\nDigite sua escolha: "))
# ============= APLICAÇÃO RECONHECIMENTO ===========================
    if ferramenta == 1:
        while True:
            # ================= MENU =================
            print("\n [1] The Harvester")
            print(" [2] Emailharvester")
            print(" [3] Reconhecimento DNS")
            print(" [4] Whois")
            print(" [5] Nmap")
            print(" [6] Masscan")
            print(" [7] Amap")
            print(" [8] Smbmap")
            print(" [9] Dnsrecon")
            print(" [10] enum4linux")
            print(" [11] Gobuster")
            print(" [0] Sair\n")

            n = int(input("Digite a opção: "))
        # ============== SCRIPTS ==================
            if n == 1:
                the_harvester()
            elif n == 2:
                emailharvester()
            elif n == 3:
                reconhecimento_dns()
            elif n == 4:
                whois()
            elif n == 5:
                nmap()
            elif n == 6:
                masscan()
            elif n == 7:
                amap()
            elif n == 8:
                smbmap()
            elif n == 9:
                dnsrecon()
            elif n == 10:
                enum4linux()
            elif n == 11:
                gobuster()
            elif n == 0:
                break
# ============== APLICAÇÃO VULNERABILIDADE ==================
    elif ferramenta == 2:
        while True:
            # ================= MENU =================
            print("\n [1] CAT")
            print(" [2] Cisco Torch")
            print(" [3] cge.pl")
            print(" [4] Cisco Ocs")
            print(" [5] Oracle Scanner")
            print(" [6] Sfuzz")
            print(" [7] Exploit DB")
            print(" [8] OpenVAS")
            print(" [0] Sair\n")

            n = int(input("Digite a opção: "))

            if n == 1:
                cat()
            elif n == 2:
                cisco_torch()
            elif n == 3:
                cgepl()
            elif n == 4:
                ciscoocs()
            elif n == 5:
                oscanner()
            elif n == 6:
                sfuzz()
            elif n == 7:
                exploitdb()
            elif n == 8:
                openvas()
            elif n == 0:
                break
    elif ferramenta == 3:
        while True:
            print("\n [1] John the Ripper (Hash cracking)")
            print(" [2] Medusa")
            print(" [0] Sair\n")

            n = int(input("Digite a opção: "))
            if n == 1:
                john()
            elif n == 2:
                medusa()
            elif n == 0:
                break
    elif ferramenta == 0:
        print("Obrigado por usar!")
        break
    else:
        print("Digite uma opção Válida")
>>>>>>> 566301831c7e12d4742ad7ba4acb5f957ea723ca
