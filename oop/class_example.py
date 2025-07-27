import random
from colorama import Fore, Back, Style, init
import re
init(autoreset = True)

class Message:
    def __init__(self, text):
        self.text = text

    def print(self):
        self._console_output(self.text)

   
    def whisper(self):
        self._console_output(self.text.lower().replace("!", ""))

    def _console_output(self, text):
        print(text)


class ColorMessage(Message):
    def __init__(self, text, color = Fore.RESET):
        super().__init__(text)
        self.color = color

    def _console_output(self, text):
        print(self.color + text)

class ScreamMessage(ColorMessage):
    def print(self):
        print(self.color + re.sub(r'(.)', "\\1 ", self.text).upper())

valid_colors = [Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX]

messages = [
    Message("Привет!"),
    ScreamMessage("Хай нигга))", Fore.RED),
    ColorMessage("Давай досвидания!!!", random.choice(valid_colors)),
    ColorMessage("Давай досвидания!!!"),
    Message("Hello there"),
]

for m in messages:
    m.print()


