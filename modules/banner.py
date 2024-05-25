from colorama import Fore, Back, Style
import platform, os
num = Fore.LIGHTYELLOW_EX
brak = Fore.LIGHTBLUE_EX
text = Fore.LIGHTRED_EX
custom = Fore.LIGHTCYAN_EX
backcolor = Back.LIGHTBLUE_EX
class Menu:

    MenuPrimary = f"""
{brak}[{num}1{brak}]{text} Ch4120N DNS                        {brak}[{num}9{brak}]{text} OpenDNS Home               {brak}[{num}17{brak}]{text} Yandex DNS
{brak}[{num}2{brak}]{text} Charon Security Agency V1          {brak}[{num}10{brak}]{text} Cloudflare DNS            {brak}[{num}18{brak}]{text} DNS.Watch
{brak}[{num}3{brak}]{text} Charon Security Agency V2          {brak}[{num}11{brak}]{text} Comodo Secure DNS         {brak}[{num}19{brak}]{text} Level 3 DNS
{brak}[{num}4{brak}]{text} Shecan DNS                         {brak}[{num}12{brak}]{text} CleanBrowsing DNS         {brak}[{num}20{brak}]{text} Oracle Dyn DNS
{brak}[{num}5{brak}]{text} Electro DNS                        {brak}[{num}13{brak}]{text} Alternate DNS             {brak}[{num}21{brak}]{text} UncensoredDNS DNS
{brak}[{num}6{brak}]{text} 403 DNS                            {brak}[{num}14{brak}]{text} AdGuard DNS               {brak}[{num}22{brak}]{text} Neustar Security DNS
{brak}[{num}7{brak}]{text} Google Public DNS                  {brak}[{num}15{brak}]{text} Verisign DNS              {brak}[{num}23{brak}]{text} Green Team DNS
{brak}[{num}8{brak}]{text} Quad9 DNS                          {brak}[{num}16{brak}]{text} OpenNIC DNS               {brak}[{num}24{brak}]{text} Safe DNS

{brak}[{num}97{brak}]{text} Custom                            {brak}[{num}98{brak}]{text} Deafult (DHCP)            {brak}[{num}99{brak}]{text} Exit
"""

class AsciiArt:
    if platform.system().lower() == "windows":
        os.system('cls')
    else:
        os.system('clear')
    Logo = Fore.LIGHTCYAN_EX+fr"""
                                 (        ) (                                            
   (      )                      )\ )  ( /( )\ )     (      )                            
   )\  ( /(    ) (              (()/(  )\()|()/(     )\  ( /(    )       (  (    (  (    
 (((_) )\())( /( )(   (   (      /(_))((_)\ /(_))  (((_) )\())( /(  (    )\))(  ))\ )(   
 )\___((_)\ )(_)|()\  )\  )\ )  (_))_  _((_|_))    )\___((_)\ )(_)) )\ )((_))\ /((_|()\  
((/ __| |(_|(_)_ ((_)((_)_(_/(   |   \| \| / __|  ((/ __| |(_|(_)_ _(_/( (()(_|_))  ((_) 
 | (__| ' \/ _` | '_/ _ \ ' \))  | |) | .` \__ \   | (__| ' \/ _` | ' \)) _` |/ -_)| '_|
  \___|_||_\__,_|_| \___/_||_|   |___/|_|\_|___/    \___|_||_\__,_|_||_|\__, |\___||_|    
                                                                        |___/

                                                                    {backcolor}{Fore.LIGHTMAGENTA_EX}Version: 1.0{Back.RESET}
                                                                    {backcolor}{Fore.LIGHTMAGENTA_EX}Programmer: Ch4120N{Back.RESET}
"""



# print(AsciiArt.Logo)
# print(Menu.MenuPrimary)