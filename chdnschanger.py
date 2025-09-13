#!/bin/python3

"""
  Charon DNS Changer 	    : 	Easy Changing DNS (Windows/Linux)
  Author                 	: 	Ch4120N
  Version                	: 	2.5.1
  Github                 	: 	https://github.com/Ch4120N/Charon-DNS-Changer
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

     Copyright (C) 2025  CH4120N (https://github.com/Ch4120N)

"""


import re
import os
import subprocess
import sys
import ctypes
import shutil
import modules.globalConfig as globalConfig
from pathlib import Path
from modules.banner import Menu, AsciiArt, BACK2MENU_INPUT, INPUTS_COLOR, CUSTOM_TEXT_COLOR
from modules.config import Config as config
from modules.decorators import INFO, INPUT, ERROR, SUCCESS, WARNING
from modules.utils import *
try:
    from colorama import Fore, Back, init
    init()
except:
    print("[ - ] Please Install colorama package: python -m pip install colorama")


class CharonDNSChanger:
    def __init__(self):
        self.SCRIPT_DIR = Path(__file__).resolve().parent
        self.BACKUP_DIR = str(str(self.SCRIPT_DIR) +
                              DIRECTORY_SEPARATOR + 'backup')

    def initialize(self):
        if (sys.platform.lower() != 'win32'):
            if (not os.path.exists(self.BACKUP_DIR)):
                try:
                    os.makedirs(self.BACKUP_DIR)
                except:
                    pass

        if (not self.check_privilege()):
            print(AsciiArt.miniLogo)
            ERROR(
                'You need to run this script as the root user in Linux/Or administrator user in Windows')
            return

        globalConfig.OS = self.check_os()
        if (globalConfig.OS == 'win'):
            globalConfig.INTERFACE = self.getPrimaryInterface()

        while True:
            clear_screen()
            print(AsciiArt.Logo)
            if (globalConfig.OS == 'win'):
                INFO(
                    f'Primary network adapter: {CUSTOM_TEXT_COLOR}{self.getPrimaryInterface()}')
            INFO(f'Current DNS: {INPUTS_COLOR}{self.getCurrentDNS()}\n')
            print(Menu.MenuPrimary)

            choice = str(colorizeInput(INPUT('Select the option [01-99] > ')))
            otherChoices = self.getNormalizedChoice(choice)

            if (choice == "97"):
                clear_screen()
                print(AsciiArt.Logo)
                customDNSResult = self.customDNS()
                clear_screen()
                print(AsciiArt.miniLogo)
                if (customDNSResult):
                    SUCCESS('Custom DNS applied successfully\n')
                    colorizeInput(INPUT(BACK2MENU_INPUT))
                else:
                    ERROR('Custom DNS could not be applied\n')
                    colorizeInput(INPUT(BACK2MENU_INPUT))

            elif (choice == "98"):
                clear_screen()
                print(AsciiArt.Logo)
                resetDNSResult = self.resetDNS2DHCP()
                clear_screen()
                print(AsciiArt.miniLogo)
                if (resetDNSResult):
                    SUCCESS('Automatic DNS (DHCP) applied successfully\n')
                    colorizeInput(INPUT(BACK2MENU_INPUT))
                else:
                    ERROR('Failed to apply automatic DNS (DHCP)\n')
                    colorizeInput(INPUT(BACK2MENU_INPUT))
            elif (choice == "99"):
                clear_screen()
                print(AsciiArt.Logo)
                WARNING('Program Terminated!')
                sys.exit(1)
            elif (otherChoices):
                index1, index2 = self.getDNS(otherChoices)
                if (index1 and index2):
                    listSelectedResult = self.setDNS(index1, index2)
                    clear_screen()
                    print(AsciiArt.miniLogo)
                    if (listSelectedResult):
                        SUCCESS(f'"{otherChoices}" applied successfully\n')
                        colorizeInput(INPUT(BACK2MENU_INPUT))
                    else:
                        ERROR(f'Failed to apply "{otherChoices}"\n')
                        colorizeInput(INPUT(BACK2MENU_INPUT))
            else:
                clear_screen()
                print(AsciiArt.Logo)
                ERROR('Invalid input. Please select [01-99] (e.g, 04)\n')
                colorizeInput(INPUT(BACK2MENU_INPUT))

    def check_os(self):
        return ('win' if (sys.platform.lower() == 'win32')
                else 'linux'
                )

    def check_privilege(self):
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    def getNormalizedChoice(self, text: str):
        normalized = str(int(text))  # "01" -> "1"
        return config.OPTIONS.get(normalized)

    def getPrimaryInterface(self):
        if (globalConfig.OS != 'win'):
            return

        try:
            netsh_results = subprocess.getoutput(
                'netsh interface show interface').splitlines()

            netsh_results = [line.strip()
                             for line in netsh_results if line.strip()]

            for line in netsh_results:
                columns = line.split()
                if 'Admin' in columns or 'State' in columns:
                    continue

                if 'Enabled' in columns and 'Connected' in columns:
                    interface_name = " ".join(columns[3:])
                    if any(kw.lower() in interface_name.lower() for kw in config.VIRTUAL_KEYWORDS):
                        continue
                    return interface_name
        except:
            return 'UNKNOWN'

    def getCurrentDNS(self):
        dns_list = []

        if (globalConfig.OS == "win"):
            try:
                netsh_output = subprocess.getoutput(
                    "netsh interface ip show dns").splitlines()
                for line in netsh_output:
                    match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", line)
                    if match:
                        ip = match.group(1)
                        if ip not in dns_list:
                            dns_list.append(ip)
            except:
                return (f"Error on getting current DNSs")
        else:
            try:
                with open(config.LINUX_DNS_CONFIG_PATH, "r") as f:
                    for line in f:
                        line = line.strip()
                        if line.startswith("nameserver"):
                            parts = line.split()
                            if len(parts) >= 2 and parts[1] not in dns_list:
                                dns_list.append(parts[1])
            except:
                return (f"Can't read /etc/resolv.conf")

        return ", ".join(dns_list)

    def getDNS(self, name: str):
        indexes = config.DNS_DICTIONARY.get(name)
        try:
            return indexes.get('index1'), indexes.get('index2')
        except AttributeError:
            return (None, None)

    def setDNS(self, primaryDNS: str, secondaryDNS: str):
        if (globalConfig.OS == 'win'):
            primaryResult = execute(
                f'netsh interface ip set dns "{globalConfig.INTERFACE}" static "{primaryDNS}"')
            secondaryResult = execute(
                f'netsh interface ip add dns "{globalConfig.INTERFACE}" "{secondaryDNS}" index=2')

            if (primaryResult and secondaryResult):
                return True
            else:
                return False
        else:
            try:
                shutil.move('/etc/resolv.conf', self.BACKUP_DIR +
                            DIRECTORY_SEPARATOR + 'resolv.conf.bak')
            except:
                return False

            generatedInfo = generateINFO()

            query1 = f'echo "{generatedInfo}" > {config.LINUX_DNS_CONFIG_PATH}'
            query2 = f'echo "nameserver {primaryDNS}" >> {config.LINUX_DNS_CONFIG_PATH}'
            query3 = f'echo "nameserver {primaryDNS}" >> {config.LINUX_DNS_CONFIG_PATH}'

            linuxResult = execute(f'{query1} && {query2} && {query3}')

            if (linuxResult):
                return True
            return False

    def resetDNS2DHCP(self):
        if (globalConfig.OS == 'win'):
            winDHCP = execute(
                f'netsh interface ip set dns name="{globalConfig.INTERFACE}" source=dhcp')
            if (winDHCP):
                return True
            return False
        else:
            try:
                shutil.move(self.BACKUP_DIR + DIRECTORY_SEPARATOR +
                            'resolv.conf.bak', '/etc/resolv.conf')
            except:
                return False
            return True

    def checkIPv4(self, nameserver: str):
        if (config.IPv4_REGEX.fullmatch(nameserver)):
            return True
        return False

    def customDNS(self):
        primaryDNS = colorizeInput(INPUT('Primary DNS (e.g., 8.8.8.8) > '))
        if (not self.checkIPv4(primaryDNS)):
            ERROR('Invalid DNS address. Please enter a valid IP (e.g., 8.8.8.8)')
            colorizeInput(BACK2MENU_INPUT)
            return False
        secondaryDNS = colorizeInput(INPUT('Secondary DNS (e.g., 8.8.4.4) > '))
        if (not self.checkIPv4(secondaryDNS)):
            ERROR('Invalid DNS address. Please enter a valid IP (e.g., 8.8.4.4)')
            colorizeInput(BACK2MENU_INPUT)
            return False
        if (self.setDNS(primaryDNS, secondaryDNS)):
            return True
        return False


if __name__ == '__main__':
    ChDNSChanger = CharonDNSChanger()
    ChDNSChanger.initialize()
