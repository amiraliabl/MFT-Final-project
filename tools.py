from os import system
from colorama import Fore


def ClearTerminal():
    system('cls')


def Wait():
    input('press enter to contiue !!!')


def add_line():
    print()


def ColoredNotification(text, color):
    if color == 'red':
        return (Fore.RED+text+Fore.WHITE)
    elif color == 'green':
        return (Fore.GREEN+text+Fore.WHITE)
    elif color == 'blue':
        return (Fore.BLUE+text+Fore.WHITE)
    