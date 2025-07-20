import argparse
import re
from colorama import Fore, Back, Style, init
init(autoreset = True)

separ1 = r"[\W]"
separ2 = r"\w"
separ3 = r"[^\w\s]"


def show_bar_result(key, max_letters, max_value):
    percent = words_map[key] / max_value * 100
    if percent >= float(args.limit): 
        print(f"{Fore.LIGHTWHITE_EX}{key}{Fore.RESET} {" " * (max_letters - len(key))} {'*' * int(percent)} {Fore.GREEN}({round(percent, 2)}%)")

def dict_magic(i): # ЭТО ИНДЕКС КОРТЕЖА (ВЕКТОРА)
    return dict(sorted(words_map.items(), key=lambda item: item[i], reverse=True))

def show_simple_result(key, max_value):
    percent = words_map[key] / max_value * 100
    if percent >= float(args.limit):
        print(f"{Fore.LIGHTWHITE_EX}{key}{Fore.RESET} {Fore.GREEN}-{Fore.RESET} {words_map[key]} {Fore.GREEN}({round(percent, 2)}%)")


words_map = {}
argsParser = argparse.ArgumentParser()
argsParser.add_argument(
    '-f', '--file-name',
    help=".txt file name.",
    required=True,
)
argsParser.add_argument(
    '-t', '--type-stat',
    help='type of statistic. By default is word',
    required=False,
    choices=['word', 'letter', 'punct'],
    default='word'
)
argsParser.add_argument(
    '-s', '--sort-type',
    help='type of statistic sort. By default is value',
    required=False,
    choices=['value', 'key'],
    default='value'
)
argsParser.add_argument(
    '-v', '--view-type',
    help='type of view statistic diagram. By default is simple',
    required=False,
    choices=['simple', 'bar'],
    default='simple'
)
argsParser.add_argument(
    '-l', '--limit',
    help='entrance value limit (in percent). By default is 1% (FOR CORRECT WORK PICK ONLY 1-99)',
    required=False,
    default='0'
)
args = argsParser.parse_args()
print(args.type_stat, args.file_name)
def reading(n, s):
    print(Back.RED + Fore.BLACK + "Reading file...")
    with open(n, "r", encoding="utf-8") as file:
        for line in file:
            flag = 0
            words_line_parts = re.split(s, line)
            clear_words_line_parts = [item for item in words_line_parts if item]
            for i in clear_words_line_parts:
                if clear_words_line_parts[flag] in words_map:
                    words_map[i] += 1
                else:
                    words_map[i] = 1
                flag += 1
def reading2(n, s):
    print(Back.RED + Fore.BLACK + "Reading file...")
    with open(n, "r", encoding="utf-8") as file:
        for line in file:
            flag = 0
            words_line_parts = list(line)
            clear_words_line_parts = [item for item in words_line_parts if re.match(s, item)]
            for i in clear_words_line_parts:
                if clear_words_line_parts[flag] in words_map:
                    words_map[i] += 1
                else:
                    words_map[i] = 1   
                flag += 1            
     
if args.type_stat == 'word':
    reading(args.file_name, separ1)
elif args.type_stat == 'letter':
    reading2(args.file_name, separ2)
elif args.type_stat == 'punct':
    reading2(args.file_name, separ3)
if args.sort_type == 'key':
    max_letters = len(max(words_map, key=len))
    max_value = max(words_map.values()) 
    if args.view_type == "simple":
        for y in dict_magic(0):
            show_simple_result(y, max_value)
    else:
        print()
        print(Back.RED + Fore.BLACK + "100% - 100х*")
        print()
        for y in dict_magic(0):
            show_bar_result(y, max_letters, max_value)
elif args.sort_type == 'value':
    max_value = max(words_map.values())
    max_letters = len(max(words_map, key=len))
    if args.view_type == "simple":
        for y in dict_magic(1):
            show_simple_result(y, max_value)
    else:
        print()
        print(Back.RED + Fore.BLACK + "100% - 100х*")
        print()

        for y in dict_magic(1): 
            show_bar_result(y, max_letters, max_value)


