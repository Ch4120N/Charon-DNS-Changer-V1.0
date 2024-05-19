#!/bin/python3

"""
  Charon DNS Changer V1 	: 	Easy Changing DNS (Windows/Linux)
  Author                 	: 	Ch4120N
  Version                	: 	2.3.5
  Github                 	: 	https://github.com/Ch4120N/Charon-DNS-Changer-V1.0
"""


"""                  GNU GENERAL PUBLIC LICENSE
                   Version 3, 29 June 2007

   Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
   Everyone is permitted to copy and distribute verbatim copies
   of this license document, but changing it is not allowed.

                        Preamble

   The GNU General Public License is a free, copyleft license for
   software and other kinds of works.

   The licenses for most software and other practical works are designed
   to take away your freedom to share and change the works.  By contrast,
   the GNU General Public License is intended to guarantee your freedom to
   share and change all versions of a program--to make sure it remains free
   software for all its users.  We, the Free Software Foundation, use the
   GNU General Public License for most of our software; it applies also to
   any other work released this way by its authors.  You can apply it to
   your programs, too.

   When we speak of free software, we are referring to freedom, not
   price.  Our General Public Licenses are designed to make sure that you
   have the freedom to distribute copies of free software (and charge for
   them if you wish), that you receive source code or can get it if you
   want it, that you can change the software or use pieces of it in new
   free programs, and that you know you can do these things.

   To protect your rights, we need to prevent others from denying you
   these rights or asking you to surrender the rights.  Therefore, you have
   certain responsibilities if you distribute copies of the software, or if
   you modify it: responsibilities to respect the freedom of others.

   For example, if you distribute copies of such a program, whether
   gratis or for a fee, you must pass on to the recipients the same
   freedoms that you received.  You must make sure that they, too, receive
   or can get the source code.  And you must show them these terms so they
   know their rights.

   Developers that use the GNU GPL protect your rights with two steps:
   (1) assert copyright on the software, and (2) offer you this License
   giving you legal permission to copy, distribute and/or modify it.

   For the developers' and authors' protection, the GPL clearly explains
   that there is no warranty for this free software.  For both users' and
   authors' sake, the GPL requires that modified versions be marked as
   changed, so that their problems will not be attributed erroneously to
   authors of previous versions.

   Some devices are designed to deny users access to install or run
   modified versions of the software inside them, although the manufacturer
   can do so.  This is fundamentally incompatible with the aim of
   protecting users' freedom to change the software.  The systematic
   pattern of such abuse occurs in the area of products for individuals to
   use, which is precisely where it is most unacceptable.  Therefore, we
   have designed this version of the GPL to prohibit the practice for those
   products.  If such problems arise substantially in other domains, we
   stand ready to extend this provision to those domains in future versions
   of the GPL, as needed to protect the freedom of users.

   Finally, every program is threatened constantly by software patents.
   States should not allow patents to restrict development and use of
   software on general-purpose computers, but in those that do, we wish to
   avoid the special danger that patents applied to a free program could
   make it effectively proprietary.  To prevent this, the GPL assures that
   patents cannot be used to render the program non-free.

   The precise terms and conditions for copying, distribution and
   modification follow.

     Copyright (C) 2022  CH4120N (https://github.com/Ch4120N)

"""


import os
import subprocess
import platform
import sys
import ctypes
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
    SYSTEM = None
    def __init__(self):
        if self.Check_AdminPriviliges():
            self.Check_System()
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
                        self.clear_screen()
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
        else:
            sys.exit(Fore.RED+"[-] You need to use the root user in Linux or administrator user in Windows.")
            


        # print(other_choice)
        # elif self.getdns(choice):
    def Check_AdminPriviliges(self):
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        
        return is_admin
    def Check_System(self):
        if "win" in platform.system().lower():
            self.SYSTEM = "win"
        else:
            self.SYSTEM = "linux"
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
        if self.SYSTEM == "win":
            subprocess.getoutput(f'netsh interface ip set dns name="{self.INTERFACE_SELECTED}" static "{primery_DNS}"')
            subprocess.getoutput(f'netsh interface ip add dns name="{self.INTERFACE_SELECTED}" "{secoundry_DNS}" index=2')
        else:
            subprocess.getoutput(f'echo "# Generated By Charon DNS Changer" > /etc/resolv.conf && echo "nameserver {primery_DNS}" >> /etc/resolv.conf && echo "nameserver {secoundry_DNS}" >> /etc/resolv.conf')

    def getdns(self, select:str):
        other_choice = []
        for i in config.selected.keys():
            other_choice.append(i)
        
        try:
            return config.selected.get(other_choice[int(select)-1])
        except:
            return

    def Restoration_DNS(self):
        if self.SYSTEM == "win":
            with open('Settings.json', 'r') as f:
                data = f.read()
            
            obj = json.loads(data)
            for i in obj:
                if self.INTERFACE_SELECTED in ', '.join(str(x) for x in i.values()):
                    pattern = ', '.join(str(x) for x in i.values())
                    data_listed = pattern.split(', ')
            if self.INTERFACE_SELECTED == data_listed[0]:
                self.set_dns(data_listed[1], data_listed[2])
        else:
            self.set_dns('1.1.1.1', '1.0.0.1')


    def GetInterfaceName(self):
        if self.SYSTEM == "win":
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