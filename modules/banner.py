from colorama import Fore, Back

# Define standard colors for different elements of the menu and banners
BACKGROUND_COLOR = Back.LIGHTBLUE_EX      # Background color for highlights
BRACKETS_COLOR = Fore.LIGHTBLUE_EX        # Color for brackets [] in menus
CUSTOM_COLOR = Fore.LIGHTCYAN_EX          # Custom accent color for banners
CUSTOM_TEXT_COLOR = Fore.LIGHTGREEN_EX    # Custom text color for emphasis
DEFAULT_SUB_BANNER_COLOR = Fore.LIGHTWHITE_EX  # Default color for sub-banners
FOREGROUND_RESET = Fore.RESET             # Reset color to default terminal color
NUMBERS_COLOR = Fore.LIGHTYELLOW_EX       # Color for numeric menu options
TEXTS_COLOR = Fore.LIGHTRED_EX            # Color for general text in menus
INPUTS_COLOR = Fore.LIGHTMAGENTA_EX       # Color for user input prompts

# Predefined prompt to return to the main menu, with colorized brackets and text
BACK2MENU_INPUT = f'{DEFAULT_SUB_BANNER_COLOR}Press {BRACKETS_COLOR}[{TEXTS_COLOR}ENTER{BRACKETS_COLOR}]{DEFAULT_SUB_BANNER_COLOR} key for back to main menu ...'


class Menu:
    """
    Contains text templates for the menu system.
    MenuPrimary: main DNS selection menu with options numbered and color-coded.
    """
    MenuPrimary = f"""
  {BRACKETS_COLOR}[{NUMBERS_COLOR}01{BRACKETS_COLOR}]{TEXTS_COLOR} Ch4120N DNS                        {BRACKETS_COLOR}[{NUMBERS_COLOR}09{BRACKETS_COLOR}]{TEXTS_COLOR} OpenDNS Home              {BRACKETS_COLOR}[{NUMBERS_COLOR}17{BRACKETS_COLOR}]{TEXTS_COLOR} Yandex DNS
  {BRACKETS_COLOR}[{NUMBERS_COLOR}02{BRACKETS_COLOR}]{TEXTS_COLOR} Charon Security Agency V1          {BRACKETS_COLOR}[{NUMBERS_COLOR}10{BRACKETS_COLOR}]{TEXTS_COLOR} Cloudflare DNS            {BRACKETS_COLOR}[{NUMBERS_COLOR}18{BRACKETS_COLOR}]{TEXTS_COLOR} DNS.Watch
  {BRACKETS_COLOR}[{NUMBERS_COLOR}03{BRACKETS_COLOR}]{TEXTS_COLOR} Charon Security Agency V2          {BRACKETS_COLOR}[{NUMBERS_COLOR}11{BRACKETS_COLOR}]{TEXTS_COLOR} Comodo Secure DNS         {BRACKETS_COLOR}[{NUMBERS_COLOR}19{BRACKETS_COLOR}]{TEXTS_COLOR} Level 3 DNS
  {BRACKETS_COLOR}[{NUMBERS_COLOR}04{BRACKETS_COLOR}]{TEXTS_COLOR} Shecan DNS                         {BRACKETS_COLOR}[{NUMBERS_COLOR}12{BRACKETS_COLOR}]{TEXTS_COLOR} CleanBrowsing DNS         {BRACKETS_COLOR}[{NUMBERS_COLOR}20{BRACKETS_COLOR}]{TEXTS_COLOR} Oracle Dyn DNS
  {BRACKETS_COLOR}[{NUMBERS_COLOR}05{BRACKETS_COLOR}]{TEXTS_COLOR} Electro DNS                        {BRACKETS_COLOR}[{NUMBERS_COLOR}13{BRACKETS_COLOR}]{TEXTS_COLOR} Alternate DNS             {BRACKETS_COLOR}[{NUMBERS_COLOR}21{BRACKETS_COLOR}]{TEXTS_COLOR} UncensoredDNS DNS
  {BRACKETS_COLOR}[{NUMBERS_COLOR}06{BRACKETS_COLOR}]{TEXTS_COLOR} 403 DNS                            {BRACKETS_COLOR}[{NUMBERS_COLOR}14{BRACKETS_COLOR}]{TEXTS_COLOR} AdGuard DNS               {BRACKETS_COLOR}[{NUMBERS_COLOR}22{BRACKETS_COLOR}]{TEXTS_COLOR} Neustar Security DNS
  {BRACKETS_COLOR}[{NUMBERS_COLOR}07{BRACKETS_COLOR}]{TEXTS_COLOR} Google Public DNS                  {BRACKETS_COLOR}[{NUMBERS_COLOR}15{BRACKETS_COLOR}]{TEXTS_COLOR} Verisign DNS              {BRACKETS_COLOR}[{NUMBERS_COLOR}23{BRACKETS_COLOR}]{TEXTS_COLOR} Green Team DNS
  {BRACKETS_COLOR}[{NUMBERS_COLOR}08{BRACKETS_COLOR}]{TEXTS_COLOR} Quad9 DNS                          {BRACKETS_COLOR}[{NUMBERS_COLOR}16{BRACKETS_COLOR}]{TEXTS_COLOR} OpenNIC DNS               {BRACKETS_COLOR}[{NUMBERS_COLOR}24{BRACKETS_COLOR}]{TEXTS_COLOR} Safe DNS
  
  {BRACKETS_COLOR}[{NUMBERS_COLOR}97{BRACKETS_COLOR}]{TEXTS_COLOR} Custom                             {BRACKETS_COLOR}[{NUMBERS_COLOR}98{BRACKETS_COLOR}]{TEXTS_COLOR} Default (DHCP)            {BRACKETS_COLOR}[{NUMBERS_COLOR}99{BRACKETS_COLOR}]{TEXTS_COLOR} Exit
{FOREGROUND_RESET}"""  # Reset color at the end to avoid affecting terminal


class AsciiArt:
    """
    Stores ASCII art templates for banners and logos.
    Logo: Large banner displayed on program start.
    miniLogo: Smaller banner for secondary screens or notifications.
    """

    # Large decorative ASCII art logo with version and author info
    Logo = CUSTOM_COLOR + fr"""
                                                                                 
     _____ _                      ____  _____ _____    _____ _                       
    |     | |_ ___ ___ ___ ___   |    \|   | |   __|  |     | |_ ___ ___ ___ ___ ___ 
    |   --|   | .'|  _| . |   |  |  |  | | | |__   |  |   --|   | .'|   | . | -_|  _|
    |_____|_|_|__,|_| |___|_|_|  |____/|_|___|_____|  |_____|_|_|__,|_|_|_  |___|_|  
                                                                        |___|        
                    {NUMBERS_COLOR}╔════════════════════════════════════════════╗
                    {NUMBERS_COLOR}║             {CUSTOM_COLOR}Charon DNS Changer             {NUMBERS_COLOR}║
                    {NUMBERS_COLOR}║       {TEXTS_COLOR}Powerful Tool For Changing DNS       {NUMBERS_COLOR}║
                    {NUMBERS_COLOR}║  {CUSTOM_TEXT_COLOR}Author  :  {DEFAULT_SUB_BANNER_COLOR}AmirHossein Ghanami {BRACKETS_COLOR}({TEXTS_COLOR}Ch4120N{BRACKETS_COLOR})  {NUMBERS_COLOR}║
                    {NUMBERS_COLOR}║  {CUSTOM_TEXT_COLOR}Github  :  {DEFAULT_SUB_BANNER_COLOR}Github.com/Ch4120N             {NUMBERS_COLOR}║
                    {NUMBERS_COLOR}║  {CUSTOM_TEXT_COLOR}Version :  {DEFAULT_SUB_BANNER_COLOR}1.1                            {NUMBERS_COLOR}║
                    {NUMBERS_COLOR}╚════════════════════════════════════════════╝{FOREGROUND_RESET}
"""

    # Smaller ASCII art logo for minimal display or secondary menus
    miniLogo = TEXTS_COLOR + fr"""
    ░█▀▀░█░█░█▀█░█▀▄░█▀█░█▀█░░░█▀▄░█▀█░█▀▀░░░█▀▀░█░█░█▀█░█▀█░█▀▀░█▀▀░█▀▄
    ░█░░░█▀█░█▀█░█▀▄░█░█░█░█░░░█░█░█░█░▀▀█░░░█░░░█▀█░█▀█░█░█░█░█░█▀▀░█▀▄
    ░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀░▀░░░▀▀░░▀░▀░▀▀▀░░░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀  
                                                            {DEFAULT_SUB_BANNER_COLOR}Version: 1.1
"""
