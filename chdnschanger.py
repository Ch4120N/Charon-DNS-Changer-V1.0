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
from modules.banner import (
    Menu,
    AsciiArt,
    BACK2MENU_INPUT,
    INPUTS_COLOR,
    CUSTOM_TEXT_COLOR,
)
from modules.config import Config as config
from modules.decorators import INFO, INPUT, ERROR, SUCCESS, WARNING
from modules.utils import *

# Attempt to import and initialize colorama for colored terminal output
try:
    from colorama import Fore, Back, init

    init()
except:
    print("[ - ] Please Install colorama package: python -m pip install colorama")


class CharonDNSChanger:
    """
    Main class to handle DNS changes for Windows and Linux systems.
    Provides functionality for setting custom DNS, restoring DHCP,
    and viewing current DNS settings.
    """

    def __init__(self):
        # Define script directory
        self.SCRIPT_DIR = Path(__file__).resolve().parent
        # Define backup directory for Linux resolv.conf or other backups
        self.BACKUP_DIR = str(str(self.SCRIPT_DIR) + DIRECTORY_SEPARATOR + "backup")

    def initialize(self):
        """
        Initializes the program, checks OS, privileges, and handles
        the main interactive menu for DNS operations.
        """
        # On Linux, create backup directory if it does not exist
        if sys.platform.lower() != "win32":
            if not os.path.exists(self.BACKUP_DIR):
                try:
                    os.makedirs(self.BACKUP_DIR)
                except:
                    pass

        # Ensure the script is run with admin/root privileges
        if not self.check_privilege():
            print(AsciiArt.miniLogo)
            ERROR(
                "You need to run this script as the root user in Linux/Or administrator user in Windows"
            )
            return

        # Detect operating system
        globalConfig.OS = self.check_os()
        # On Windows, determine the primary network interface
        if globalConfig.OS == "win":
            globalConfig.INTERFACE = self.getPrimaryInterface()

        # Main loop to display menu and handle user choices
        while True:
            clear_screen()
            print(AsciiArt.Logo)

            # Display primary interface if Windows
            if globalConfig.OS == "win":
                INFO(
                    f"Primary network adapter: {CUSTOM_TEXT_COLOR}{self.getPrimaryInterface()}"
                )
            # Display current DNS configuration
            INFO(f"Current DNS: {INPUTS_COLOR}{self.getCurrentDNS()}\n")
            print(Menu.MenuPrimary)

            # Get user input choice
            choice = str(colorizeInput(INPUT("Select the option [01-99] > ")))
            otherChoices = self.getNormalizedChoice(choice)

            # Custom DNS option
            if choice == "97":
                clear_screen()
                print(AsciiArt.Logo)
                customDNSResult = self.customDNS()
                clear_screen()
                print(AsciiArt.miniLogo)
                if customDNSResult:
                    SUCCESS("Custom DNS applied successfully\n")
                    colorizeInput(INPUT(BACK2MENU_INPUT))
                else:
                    ERROR("Custom DNS could not be applied\n")
                    colorizeInput(INPUT(BACK2MENU_INPUT))

            # Reset to automatic DNS (DHCP)
            elif choice == "98":
                clear_screen()
                print(AsciiArt.Logo)
                resetDNSResult = self.resetDNS2DHCP()
                clear_screen()
                print(AsciiArt.miniLogo)
                if resetDNSResult:
                    SUCCESS("Automatic DNS (DHCP) applied successfully\n")
                    colorizeInput(INPUT(BACK2MENU_INPUT))
                else:
                    ERROR("Failed to apply automatic DNS (DHCP)\n")
                    colorizeInput(INPUT(BACK2MENU_INPUT))

            # Exit program
            elif choice == "99":
                clear_screen()
                print(AsciiArt.Logo)
                WARNING("Program Terminated!")
                sys.exit(1)

            # Predefined DNS choices from config
            elif otherChoices:
                index1, index2 = self.getDNS(otherChoices)
                if index1 and index2:
                    listSelectedResult = self.setDNS(index1, index2)
                    clear_screen()
                    print(AsciiArt.miniLogo)
                    if listSelectedResult:
                        SUCCESS(f'"{otherChoices}" applied successfully\n')
                        colorizeInput(INPUT(BACK2MENU_INPUT))
                    else:
                        ERROR(f'Failed to apply "{otherChoices}"\n')
                        colorizeInput(INPUT(BACK2MENU_INPUT))
            else:
                # Invalid input handler
                clear_screen()
                print(AsciiArt.Logo)
                ERROR("Invalid input. Please select from options [01-99] (e.g, 04)\n")
                colorizeInput(INPUT(BACK2MENU_INPUT))

    def check_os(self):
        """
        Detects the current operating system.
        Returns 'win' for Windows or 'linux' for Linux.
        """
        return "win" if (sys.platform.lower() == "win32") else "linux"

    def check_privilege(self):
        """
        Checks if the script is run with administrative/root privileges.
        Returns True if admin/root, False otherwise.
        """
        try:
            is_admin = os.getuid() == 0  # Linux root check
        except AttributeError:
            # Windows admin check
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
        return is_admin

    def getNormalizedChoice(self, text: str):
        """
        Converts user input like "01" to "1" and retrieves the corresponding
        DNS option from the config dictionary.
        """
        normalized = str(int(text))  # "01" -> "1"
        return config.OPTIONS.get(normalized)

    def getPrimaryInterface(self):
        """
        Retrieves the primary network interface name on Windows.
        Skips virtual adapters based on keywords in config.
        """
        if globalConfig.OS != "win":
            return

        try:
            netsh_results = subprocess.getoutput(
                "netsh interface show interface"
            ).splitlines()

            netsh_results = [line.strip() for line in netsh_results if line.strip()]

            for line in netsh_results:
                columns = line.split()
                if "Admin" in columns or "State" in columns:
                    continue

                if "Enabled" in columns and "Connected" in columns:
                    interface_name = " ".join(columns[3:])
                    if any(
                        kw.lower() in interface_name.lower()
                        for kw in config.VIRTUAL_KEYWORDS
                    ):
                        continue
                    return interface_name
        except:
            return "UNKNOWN"

    def getCurrentDNS(self):
        """
        Retrieves the currently configured DNS servers for the system.
        Handles both Windows and Linux.
        Returns a comma-separated string of DNS addresses.
        """
        dns_list = []

        if globalConfig.OS == "win":
            try:
                netsh_output = subprocess.getoutput(
                    "netsh interface ip show dns"
                ).splitlines()
                for line in netsh_output:
                    match = re.search(r"(\d{1,3}(?:\.\d{1,3}){3})", line)
                    if match:
                        ip = match.group(1)
                        if ip not in dns_list:
                            dns_list.append(ip)
            except:
                return f"Error on getting current DNSs"
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
                return f"Can't read /etc/resolv.conf"

        return ", ".join(dns_list)

    def getDNS(self, name: str):
        """
        Retrieves the primary and secondary DNS addresses for a given
        predefined DNS option name from the config dictionary.
        """
        indexes = config.DNS_DICTIONARY.get(name)
        try:
            return indexes.get("index1"), indexes.get("index2")
        except AttributeError:
            return (None, None)

    def setDNS(self, primaryDNS: str, secondaryDNS: str):
        """
        Sets the DNS servers on the system.
        On Windows: uses netsh commands.
        On Linux: updates /etc/resolv.conf after creating backup.
        Returns True on success, False otherwise.
        """
        if globalConfig.OS == "win":
            primaryResult = execute(
                f'netsh interface ip set dns "{globalConfig.INTERFACE}" static "{primaryDNS}"'
            )
            secondaryResult = execute(
                f'netsh interface ip add dns "{globalConfig.INTERFACE}" "{secondaryDNS}" index=2'
            )

            if primaryResult and secondaryResult:
                return True
            else:
                return False
        else:
            try:
                # Backup current resolv.conf
                shutil.move(
                    "/etc/resolv.conf",
                    self.BACKUP_DIR + DIRECTORY_SEPARATOR + "resolv.conf.bak",
                )
            except:
                return False

            generatedInfo = generateINFO()

            # Construct Linux DNS update commands
            query1 = f'echo "{generatedInfo}" > {config.LINUX_DNS_CONFIG_PATH}'
            query2 = f'echo "nameserver {primaryDNS}" >> {config.LINUX_DNS_CONFIG_PATH}'
            query3 = f'echo "nameserver {primaryDNS}" >> {config.LINUX_DNS_CONFIG_PATH}'

            linuxResult = execute(f"{query1} && {query2} && {query3}")

            if linuxResult:
                return True
            return False

    def resetDNS2DHCP(self):
        """
        Resets the DNS configuration to automatic/DHCP mode.
        Handles both Windows and Linux.
        """
        if globalConfig.OS == "win":
            winDHCP = execute(
                f'netsh interface ip set dns name="{globalConfig.INTERFACE}" source=dhcp'
            )
            if winDHCP:
                return True
            return False
        else:
            try:
                # Restore backup resolv.conf
                shutil.move(
                    self.BACKUP_DIR + DIRECTORY_SEPARATOR + "resolv.conf.bak",
                    "/etc/resolv.conf",
                )
            except:
                return False
            return True

    def checkIPv4(self, nameserver: str):
        """
        Validates if the provided string is a valid IPv4 address.
        Returns True if valid, False otherwise.
        """
        if config.IPv4_REGEX.fullmatch(nameserver):
            return True
        return False

    def customDNS(self):
        """
        Prompts the user for custom primary and secondary DNS addresses,
        validates them, and applies them to the system.
        Returns True if successful, False otherwise.
        """
        primaryDNS = colorizeInput(INPUT("Primary DNS (e.g., 8.8.8.8) > "))
        if not self.checkIPv4(primaryDNS):
            ERROR("Invalid DNS address. Please enter a valid IP (e.g., 8.8.8.8)")
            colorizeInput(BACK2MENU_INPUT)
            return False
        secondaryDNS = colorizeInput(INPUT("Secondary DNS (e.g., 8.8.4.4) > "))
        if not self.checkIPv4(secondaryDNS):
            ERROR("Invalid DNS address. Please enter a valid IP (e.g., 8.8.4.4)")
            colorizeInput(BACK2MENU_INPUT)
            return False
        if self.setDNS(primaryDNS, secondaryDNS):
            return True
        return False


if __name__ == "__main__":
    # Instantiate the DNS changer class and start the interactive menu
    ChDNSChanger = CharonDNSChanger()
    ChDNSChanger.initialize()
