import re

class ScreamMessage:
    def __init__(self, message):
        self.original_message = message

    def show(self):
        print(self.value())

    def value(self):
        return re.sub(r'(.)', "\\1 ", self.original_message.value()).upper()
