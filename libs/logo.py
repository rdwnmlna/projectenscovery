# coding=utf-8
#!/usr/bin/env python3
from colorama import Fore, Back, Style
from random import choice

logo = """
 █████╗ ███╗   ██╗██████╗ ██████╗ ██╗    ███╗██████╗  ██████╗ ████████╗███╗
██╔══██╗████╗  ██║██╔══██╗██╔══██╗██║    ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝╚██║
███████║██╔██╗ ██║██║  ██║██████╔╝██║    ██║ ██████╔╝██║   ██║   ██║    ██║
██╔══██║██║╚██╗██║██║  ██║██╔══██╗██║    ██║ ██╔══██╗██║   ██║   ██║    ██║
██║  ██║██║ ╚████║██████╔╝██║  ██║██║    ███╗██████╔╝╚██████╔╝   ██║   ███║
╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝ ╚═╝  ╚═╝╚═╝    ╚══╝╚═════╝  ╚═════╝    ╚═╝   ╚══╝v4"""

youtube_urls = [
    "WEARE UNDERGROUND TEAM - /.hookme - /.bdg-exploiters - /.hackerone-team - /.jakarta exploiters",
    ]

def print_logo():
    print(Fore.RED + Style.BRIGHT + logo + Style.RESET_ALL + Style.BRIGHT +"\n")
    print(Fore.MAGENTA + "      Created by: Andri Exploiters"+ Style.RESET_ALL + Style.BRIGHT)
    print(Fore.CYAN + "\n", "-> Saya ingin mengucapkan terima kasih kepada teman yang membantu memberi ide melalui Telegram untuk membuat fitur pada project ini agar lebih baik untuk di masadepan yang akan datang.")
    print ("\n", "-> Spesial bagi yang tidak mencium bau mawar dengan masker gas:\n    " + choice(youtube_urls))
    print(Style.RESET_ALL + Style.BRIGHT, Style.BRIGHT)
