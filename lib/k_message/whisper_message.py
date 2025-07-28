class WhisperMessage:
    def __init__(self, message):
        self.original_message = message

    def show(self):
        print(self.value())
    
    def value(self):
        return self.original_message.text.lower().replace("!", "")
