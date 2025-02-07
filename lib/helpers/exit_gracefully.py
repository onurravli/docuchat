from colorama import Fore, Style, init


def exit_gracefully():
    init()
    print(f"{Fore.YELLOW}Bye!{Style.RESET_ALL}")
    exit()
