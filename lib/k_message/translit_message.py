class TranslitMessage:
    def __init__(self, message):
        self.original_message = message

    def show(self):
        print(self.value())

    def value(self):
        words_list = {
            "а": 'a', 
            "б": 'b', 
            "в": 'v', 
            "г": 'g', 
            "д": 'd', 
            "е": 'e', 
            "ё": 'yo', 
            "ж": 'dj', 
            "з": 'z', 
            "и": 'i', 
            "й": 'q', 
            "к": 'k', 
            "л": 'l', 
            "м": 'm', 
            "н": 'n', 
            "о": 'o', 
            "п": 'p', 
            "р": 'r', 
            "с": 's', 
            "т": 't', 
            "у": 'u', 
            "ф": 'f', 
            "х": 'h', 
            "ъ": '', 
            "ь": '', 
            "э": 'ye', 
            "ю": 'uy', 
            "я": 'ya'            
        }

        uppercase_words_list = {}
        for key, value in words_list.items():
            uppercase_words_list[key.upper()] = value.upper()

        complete_words_list = {**words_list, **uppercase_words_list}

        new_word = ''

        for c in self.original_message.value():
            if c in complete_words_list:
                new_word += complete_words_list[c]
            else:
                new_word += c
        return new_word
