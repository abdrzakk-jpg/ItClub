
from colorama import Fore, Style, init
init(autoreset=True)

def make_box(text, color):
    lines = str(text).split('\n')
    max_len = max(len(line) for line in lines)
    top = f"{color}┌{'─' * (max_len + 2)}┐"
    middle = [f"{color}│ {line.ljust(max_len)} │" for line in lines]
    bottom = f"{color}└{'─' * (max_len + 2)}┘"
    return '\n'.join([top] + middle + [bottom]) + Style.RESET_ALL

# ألوان سريعة
red    = lambda txt: print(make_box(txt,Fore.RED))
green  = lambda txt: print(make_box(txt,Fore.GREEN))
blue   = lambda txt: print(make_box(txt,Fore.BLUE))
yellow = lambda txt: print(make_box(txt,Fore.YELLOW))
cyan   = lambda txt: print(make_box(txt,Fore.CYAN))
white  = lambda txt: print(make_box(txt,Fore.WHITE))


