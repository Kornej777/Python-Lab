import random
from colorama import Fore, init
init(autoreset = True)

class RainbowMessage:
    def __init__(self, message):
        self.original_message = message
        self.colorz = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX, Fore.MAGENTA]
        
    def show(self):
        print(self.value())

    def value(self):
        letter_list = []
        for c in self.original_message.value():
            letter_list.append(random.choice(self.colorz) + c)
        return "".join(letter_list)