from colorama import Fore, init
init(autoreset = True)

class ColorMessage:
    def __init__(self, message, color = Fore.GREEN):
        self.original_message = message
        self.color = color

    def show(self):
        print(self.value())

    def value(self):
        return self.color + self.original_message.value()