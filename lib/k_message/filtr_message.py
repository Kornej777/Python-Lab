import re

class FiltrMessage:
    def __init__(self, message, filtr = ['дурак']):
        self.original_message = message
        self.banlist = filtr

    def show(self):
        print(self.value())

    def value(self):
        words = []
        for word in re.findall(r'\w+', self.original_message.value()):
            if word.lower() in self.banlist:
                words.append('***')
            else:   
                words.append(word)
        return ' '.join(words)