from lib.k_message import *
import random
from colorama import Fore

class UserMessage:
    def __init__(self, message, color = Fore.RESET):
        self.original_message = message
        self.color = color

    def show(self):
        print(self.value())

    def value(self):
        return ColorMessage(
            FiltrMessage(
                self.original_message
            ), self.color
        ).value()


messages = [
    Message("Привет!"),
    ScreamMessage(
        Message("Хай нигга")
    ),
    ColorMessage(
        WhisperMessage(
            Message("Давай до свидания!!!"), 
        ), random.choice([Fore.BLACK, Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTRED_EX, Fore.LIGHTYELLOW_EX])
    ),
    TranslitMessage(
            ColorMessage(
                Message("Давай до свидания!")
            ),
    ),
    TranslitMessage(
            RainbowMessage(
                Message("Привет there")
            ),
    ),
    FiltrMessage(
        Message('дурак ты понял ДДДДа'), ['понял', 'дурак']
    ),
    ScreamMessage(
        FiltrMessage(
            Message('простафиля кушает пончик'), ['простафиля']
        )
    ),
    RainbowMessage(
        ScreamMessage(
            FiltrMessage(
                Message('опа-на здорова! Давно не виделись Братанчик'), ['братан', 'братанчик']
            )
        )
    ),
    UserMessage(
        Message('Привет дурак'), Fore.MAGENTA
    )
]

for m in messages:
    m.show()


