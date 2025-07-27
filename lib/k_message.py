import random
from colorama import Fore, init
import re
init(autoreset = True)

class Message:
    def __init__(self, text):
        self.text = text

    def show(self):
        print(self.value())

    def value(self):
        return self.text

class ColorMessage:
    def __init__(self, message, color = Fore.GREEN):
        self.original_message = message
        self.color = color

    def show(self):
        print(self.value())

    def value(self):
        return self.color + self.original_message.value()

class ScreamMessage:
    def __init__(self, message):
        self.original_message = message

    def show(self):
        print(self.value())

    def value(self):
        return re.sub(r'(.)', "\\1 ", self.original_message.text).upper()

class WhisperMessage:
    def __init__(self, message):
        self.original_message = message

    def show(self):
        print(self.value())
    
    def value(self):
        return self.original_message.text.lower().replace("!", "")

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