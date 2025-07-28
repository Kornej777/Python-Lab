class Message:
    def __init__(self, text):
        self.text = text

    def show(self):
        print(self.value())

    def value(self):
        return self.text

