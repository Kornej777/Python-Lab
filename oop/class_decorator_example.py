from lib.k_message import *
import sys
print(sys.path)


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
    RainbowMessage(
            ScreamMessage(
                Message("Давай до свидания!")
            )
    ),
    RainbowMessage(
        Message("Hello there")
    )
]

for m in messages:
    m.show()


