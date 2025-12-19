# ============= BIBLIOTECAS ASSETS ===================
import random
from art import *

# =========== BIBLIOTECAS DAS FERRAMENTAS DE RECONHECIMENTO ==========
from Reconhecimento.the_harvester import the_harvester
from Reconhecimento.emailharvester import emailharvester
from Reconhecimento.reconhecimento_dns import reconhecimento_dns
from Reconhecimento.whois import whois
from Reconhecimento.nmap import nmap
from Reconhecimento.masscan import masscan
from Reconhecimento.amap import amap
from Reconhecimento.smbmap import smbmap
from Reconhecimento.dnsrecon import dnsrecon
from Reconhecimento.enum4linux import enum4linux
from Reconhecimento.gobuster import gobuster
from Reconhecimento.smbclient import smbclient

# =========== BIBLIOTECAS DAS FERRAMENTAS DE EXPLORAR VULNERABILIDADES ==========
from Explorar_Vulnerabilidades.CAT import cat
from Explorar_Vulnerabilidades.cgepl import cgepl
from Explorar_Vulnerabilidades.cisco_torch import cisco_torch
from Explorar_Vulnerabilidades.ciscoocs import ciscoocs
from Explorar_Vulnerabilidades.exploitdb import exploitdb
from Explorar_Vulnerabilidades.openvas import openvas
from Explorar_Vulnerabilidades.oscanner import oscanner
from Explorar_Vulnerabilidades.sfuzz import sfuzz

# =========== BIBLIOTECAS DAS FERRAMENTAS DE BRUTE FORCE ==========
from Brute_Force.john import john
from Brute_Force.medusa import medusa

# =============== FUNÇÕES ===============================
# == ASSETS ==
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

# == MENU ==
def iniciar_menu():
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
    print("\nMade By 5PH1NX")

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
                print(" [8] smbmap")
                print(" [9] Dnsrecon")
                print(" [10] enum4linux")
                print(" [11] Gobuster")
                print(" [12] Smbclient")
                print(" [0] Sair\n")

                n = int(input("Digite a opção: "))

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
                elif n == 12:
                    smbclient()
                elif n == 0:
                    break
                else:
                    print("Digite uma opção válida")

        # ============= APLICAÇÃO EXPLORAR VULNERABILIDADES ===========================
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
                else:
                    print("Digite uma opção válida")

        # ============= APLICAÇÃO BRUTE FORCE ===========================
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
                else:
                    print("Digite uma opção válida")

        # ============= SAIR ===========================
        elif ferramenta == 0:
            print("Obrigado por usar!")
            break

        # ============= ERRO ===========================
        else:
            print("Digite uma opção Válida")