# ================= BIBLIOTECAS ===================
from art import *
import subprocess

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
    print("Você quer: \n [1] Escaneamento TCP \n [2] Escaneamento UDP \n [3] Escaneamento Normal")
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
        ip = input("Digite o IP do alvo: ")
        comando = ["nmap", "-sV", "-O", ip]
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
    else:
        ip = input("Digite o IP do alvo: ")
        comando = ["smbmap", "-H", ip]
        resultado = subprocess.run(comando, capture_output=True, text=True)
        print("\n====== RESULTADO =======")
        print(resultado.stdout)

        if resultado.stderr:
            print("\n====== ERRO =======")
            print(resultado.stderr)
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

# == VULNERABILIDADES ==
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

# =============== ESCOLHA DO QUAL TIPO DE SCRIPT =====================
while True:
    print("Escolha qual tipo de ferramenta você quer:\n[1] Reconhecimento \n[2] Vulnerabilidade \n[0] Sair do Programa")
    ferramenta = int(input("Digite sua escolha: "))

# ============= APLICAÇÃO RECONHECIMENTO ===========================
    if ferramenta == 1:
        while True:
        # ================= LOGO =================
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
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠙⠋⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            '''
            print(logo)
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
            elif n == 0:
                break

# ============== APLICAÇÃO VULNERABILIDADE ==================
    elif ferramenta == 2:
        while True:
        # ================= LOGO =================
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
            # ================= MENU =================
            print("\n [1] CAT")
            print(" [2] Cisco Torch")
            print(" [3] cge.pl")
            print(" [4] Cisco Ocs")
            print(" [5] Oracle Scanner")
            print(" [6] Sfuzz")
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
            elif n == 0:
                break
    elif ferramenta == 0:
        print("Obrigado por usar!")

        break
    else:
        print("Digite uma opção Válida")                                                                                                                   
