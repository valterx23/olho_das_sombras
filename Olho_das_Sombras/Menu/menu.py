# ============= BIBLIOTECAS ASSETS ===================
import random
from art import *
import os

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
from Explorar_Vulnerabilidades.sqlinjection import sqlinjection
from Explorar_Vulnerabilidades.xss import xss
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
        "Knowledge is power. And power corrupts.",
        "Code is power.",
        "Knowledge breaks walls.",
        "Trust is the real vulnerability.",
        "The system lies.",
        "Think outside the protocol.",
        "Control the flow.",
        "Freedom through code.",
        "Data never forgets."]

    return random.choice(frases)

# == MENU ==
def iniciar_menu():
    os.system('clear')
    # =============== ESCOLHA DO QUAL TIPO DE SCRIPT =====================
    while True:
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
        print("")
        print("")
        print("")
        print("\nO que você quer hoje?")
        print("\n[1] Reconhecimento \n[2] Explorar Vulnerabilidades \n[3] Brute Force")
        print("\nDigite Enter para Sair do Programa....")
        ferramenta = input("\n> ").strip()
        os.system('clear')

        # ============= APLICAÇÃO RECONHECIMENTO ===========================
        if ferramenta == "1":
            while True:
                # ================= MENU =================
                print("")
                print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⢉⣉⣉⣉⡉⠛⠷⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣠⣴⣿⣿⣿⣿⣿⡿⣿⣶⣌⠹⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠻⣧⠘⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⢹⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⠛⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⢸⡇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⢿⡆⠈⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣦⠀⠀⠈⠉⠛⠓⠲⠶⠖⠚⠋⠉⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣄⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
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
                print("\nDigite Enter para Sair....")

                n = input("\n> ").strip()

                if n == "1":
                    the_harvester()
                elif n == "2":
                    emailharvester()
                elif n == "3":
                    reconhecimento_dns()
                elif n == "4":
                    whois()
                elif n == "5":
                    nmap()
                elif n == "6":
                    masscan()
                elif n == "7":
                    amap()
                elif n == "8":
                    smbmap()
                elif n == "9":
                    dnsrecon()
                elif n == "10":
                    enum4linux()
                elif n == "11":
                    gobuster()
                elif n == "12":
                    smbclient()
                elif n == "":
                    os.system('clear')
                    break
                else:
                    print("[!] Opção inválida")

        # ============= APLICAÇÃO EXPLORAR VULNERABILIDADES ===========================
        elif ferramenta == "2":
            while True:
                # ================= MENU =================
                print("")
                print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⣀⠀⢠⡀⣿⣰⢀⣠⠴⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣙⣳⣿⣿⣿⣿⣅⣀⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⢠⣄⣤⣄⣠⣶⣿⡭⣙⣷⣿⣿⣿⣯⡉⠉⠁
⠀⠀⠀⠀⢀⣤⡶⠚⣿⣿⢡⣷⡻⣿⡺⡿⣻⣄⠀⣰⠟⢹⡟⣿⠀⠉⠀⠀
⠀⠀⢀⡴⠛⠙⣶⣾⣿⣿⡘⢿⣿⣷⣯⣟⣛⡟⠰⠁⠀⢸⡇⠘⡆⠀⠀⠀
⠀⢠⠏⠀⠀⣰⣿⣿⣿⣿⣿⣶⣍⣛⠻⠿⠟⣼⡆⠀⠀⢸⠃⠀⠀⠀⠀⠀
⠀⣿⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠘⠂⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                print("\n [1] CAT")
                print(" [2] Cisco Torch")
                print(" [3] cge.pl")
                print(" [4] Cisco Ocs")
                print(" [5] Oracle Scanner")
                print(" [6] Sfuzz")
                print(" [7] Exploit DB")
                print(" [8] OpenVAS")
                print(" [9] SQL injection Payloads")
                print(" [10] XSS Payloads")
                print("\nDigite Enter para Sair....")

                n = input("\n> ").strip()

                if n == "1":
                    cat()
                elif n == "2":
                    cisco_torch()
                elif n == "3":
                    cgepl()
                elif n == "4":
                    ciscoocs()
                elif n == "5":
                    oscanner()
                elif n == "6":
                    sfuzz()
                elif n == "7":
                    exploitdb()
                elif n == "8":
                    openvas()
                elif n == "9":
                    sqlinjection()
                elif n == "10":
                    xss()
                elif n == "":
                    os.system('clear')
                    break
                else:
                    print("[!] Opção inválida")

        # ============= APLICAÇÃO BRUTE FORCE ===========================
        elif ferramenta == "3":
            while True:
                print("")
                print('''
           ⢀⣀⣤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⠟⠉⠀⠀⠀⠈⠙⠿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠉⠛⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⡶⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠙⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                print("\n [1] John the Ripper (Hash cracking)")
                print(" [2] Medusa")
                print("\nDigite Enter para Sair....")

                n = input("\n> ").strip()

                if n == "1":
                    john()
                elif n == "2":
                    medusa()
                elif n == "":
                    os.system('clear')
                    break
                else:
                    print("[!] Opção inválida")

        # ============= SAIR ===========================
        elif ferramenta == "":
            print("\nObrigado por usar!")
            break

        # ============= ERRO ===========================
        else:
            print("[!] Opção inválida")