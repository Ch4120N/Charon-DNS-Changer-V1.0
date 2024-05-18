import os
import subprocess
import platform
import sys
import webbrowser
import socket
import ctypes
import json
from modules.banner import Menu, AsciiArt, brak
from modules.config import Config as config
try:
    from colorama import Fore, Back, init
    init()
except:
    print("Please Install colorama package: pip install colorama")


class CharonDNSChangerV1:
    INTERFACE_SELECTED = ''
    def __init__(self):
        self.INTERFACE_SELECTED = self.GetInterfaceName()
        while True:
            try:
                print(AsciiArt.Logo)
                print(Menu.MenuPrimary)
                choice = str(input(Fore.LIGHTMAGENTA_EX+"Select the option [1-99]:> "))
                # self.clear_screen()
                other_choice = self.getdns(choice)
                if choice == "97":
                    self.customdns()
                elif choice == "98":
                    print(AsciiArt.Logo)
                    self.Restoration_DNS()
                    print(f"\n{brak}[{Fore.GREEN}+{brak}]{Fore.CYAN} Reset All DNS To Default Completed Successfuly.")
                    self.exit_yn()
                elif choice == "99":
                    sys.exit(Fore.RED+'[!] Shuting Down !')
                
                elif other_choice:
                    self.clear_screen()
                    print(AsciiArt.Logo)
                    dns = self.option_selected(other_choice)
                    self.set_dns(dns[0], dns[1])
                    print(f"{brak}[{Fore.GREEN}+{brak}]{Fore.CYAN} The '{other_choice}' Have Been Set as DNS")
                    self.exit_yn()
                    # print(indexs)
                
                else:
                    print(Fore.RED+"[-] Please Select Valid Option")
                    input("\n[!] Press Enter To Continue ....")
                    self.clear_screen()
            except (KeyboardInterrupt, TypeError):
                try:
                    input("\n[!] Press Enter To Continue ....")
                except:
                    sys.exit(Fore.RED+'\n[!] Shutting Down !')

                self.clear_screen()


        # print(other_choice)
        # elif self.getdns(choice):
    
    def customdns(self):
        chd = ''
        while True:
            print(AsciiArt.Logo)
            print(Fore.LIGHTGREEN_EX+'\n[+] Please insert dns EX: 8.8.8.8,8.8.4.4\n')
            choice = input(Fore.LIGHTMAGENTA_EX+'insert DNS (EX: primitive,Secondary) > ')

            choice = choice.replace(" ", "").replace('\t', "")
            chd += choice
            choice = choice.split(',')

            if len(choice) == 2:
                self.set_dns(choice[0], choice[1])
                break
            else:
                print(Fore.LIGHTRED_EX+'\n[-] Please Enter valid DNS primitive,Secondary\n')
                input('[!] Press Enter To Continue ....')
                self.clear_screen()
        print(f"{brak}[{Fore.GREEN}+{brak}]{Fore.CYAN} The '{chd}' Have Been Set as DNS")
        self.exit_yn()
        # print(choice)

    def exit_yn(self):
        choice = input(f"\n{brak}[{Fore.YELLOW}!{brak}]{Fore.LIGHTBLUE_EX} Do you want to exit [y/N]? ")
        if choice.lower() == "y":
            sys.exit(Fore.LIGHTRED_EX+'[!] Shutting Down !')
        else:
            self.clear_screen()
            pass
    def option_selected(self, select):
        for i in config.DNS_DICTIONERY.keys():
            indexs = config.DNS_DICTIONERY.get(select)
        
        return [indexs.get("index1"), indexs.get("index2")]

    def clear_screen(self):
        if platform.system().lower() == "windows":
            os.system('cls')
        else:
            os.system('clear')
    def set_dns(self, primery_DNS:str, secoundry_DNS:str):
        subprocess.getoutput(f'netsh interface ip set dns name="{self.INTERFACE_SELECTED}" static "{primery_DNS}"')
        subprocess.getoutput(f'netsh interface ip add dns name="{self.INTERFACE_SELECTED}" "{secoundry_DNS}" index=2')
    
    def getdns(self, select:str):
        other_choice = []
        for i in config.selected.keys():
            other_choice.append(i)
        
        try:
            return config.selected.get(other_choice[int(select)-1])
        except:
            return

    def Restoration_DNS(self):
        with open('Settings.json', 'r') as f:
            data = f.read()
        
        obj = json.loads(data)
        for i in obj:
            if self.INTERFACE_SELECTED in ', '.join(str(x) for x in i.values()):
                pattern = ', '.join(str(x) for x in i.values())
                data_listed = pattern.split(', ')
        if self.INTERFACE_SELECTED == data_listed[0]:
            self.set_dns(data_listed[1], data_listed[2])


    def GetInterfaceName(self):
        if socket.gethostbyname(socket.gethostname()) == "127.0.0.1":
            # print("Please Connect To A Network")
            print(Fore.CYAN+"#"*50+"Connection Error"+"#"*50, Fore.LIGHTRED_EX+"\nPlease Connect To A Network ( Lan or Wifi )\nShutdown!")
            sys.exit(1)
        else:
            current_network = subprocess.getoutput('netsh interface show interface').split('\n')
            ssid_line = [x for x in current_network if 'Enabled' in x and "Connected" in x]
            if ssid_line:
                ssid_list = ssid_line[0].split()
                self.connected_ssid = ssid_list[-1].strip()
                self.INTERFACE_SELECTED = self.connected_ssid
                return self.connected_ssid


CharonDNSChangerV1()