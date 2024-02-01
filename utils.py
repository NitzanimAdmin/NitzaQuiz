import os
import time

from colorama import Fore, Style

INTRO_TITLE = r"""                                                                                        
 __   __     __     ______   ______     ______     ______     __  __     __     ______    
/\ "-.\ \   /\ \   /\__  _\ /\___  \   /\  __ \   /\  __ \   /\ \/\ \   /\ \   /\___  \   
\ \ \-.  \  \ \ \  \/_/\ \/ \/_/  /__  \ \  __ \  \ \ \/\_\  \ \ \_\ \  \ \ \  \/_/  /__  
 \ \_\\"\_\  \ \_\    \ \_\   /\_____\  \ \_\ \_\  \ \___\_\  \ \_____\  \ \_\   /\_____\ 
  \/_/ \/_/   \/_/     \/_/   \/_____/   \/_/\/_/   \/___/_/   \/_____/   \/_/   \/_____/ 
                                                                                          
"""


def cprint(text, fcolor, bcolor='', style=Style.RESET_ALL):
    print(f'{fcolor}{bcolor}{text}{style}')
    time.sleep(0.5)


def rainbow(text):
    colors = [Fore.RED, Fore.LIGHTYELLOW_EX, Fore.LIGHTGREEN_EX, Fore.LIGHTCYAN_EX, Fore.BLUE, Fore.MAGENTA]
    out = ""
    current_color = 0
    for letter in text:
        out = out + colors[current_color] + letter
        if letter != " ":
            current_color = (current_color + 1) % len(colors)
    print(out)
