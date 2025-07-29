import argparse
from k_gibdd import Gibdd
from colorama import Fore, init
init(autoreset = True)

argsParser = argparse.ArgumentParser()
argsParser.add_argument(
    '-c', '--count',
    help="count of gos numbers generations. By default if 1",
    required=False,
    default='1'
)
args = argsParser.parse_args()

gibdd = Gibdd()

numbers = sorted(
    [gibdd.create_number() for i in range(int(args.count))], 
    key=lambda x: (int(x.region.code), x.main_part.to_str())
)

for number in numbers:
    print(Fore.LIGHTWHITE_EX + number.main_part.first_letter() 
          + Fore.RESET + number.main_part.number_part() 
          + Fore.LIGHTWHITE_EX + number.main_part.tail_letters() 
          + Fore.RESET + '_' + number.region.code + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET)
