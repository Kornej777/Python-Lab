import argparse
from k_gibdd.state_number import Gibdd
from k_gibdd.state_number import StateNumberType
from colorama import Fore, init
init(autoreset = True)

def output_type(number):
    if gibdd.number_type(number) == StateNumberType.SUPER_COOL:
        print(
            Fore.LIGHTGREEN_EX + number.main_part.first_letter()
            + number.main_part.number_part()
            + number.main_part.tail_letters()
            + '_' + str(number.region.code)
            + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
        )

    elif gibdd.number_type(number) == StateNumberType.COOL_DIGITS:
        print(
            Fore.LIGHTWHITE_EX + number.main_part.first_letter()
            + Fore.LIGHTGREEN_EX + number.main_part.number_part() + Fore.LIGHTWHITE_EX
            + number.main_part.tail_letters() + Fore.RESET
            + '_' + str(number.region.code)
            + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
        )

    elif gibdd.number_type(number) == StateNumberType.COOL_LETTERS:
        print(
            Fore.LIGHTGREEN_EX + number.main_part.first_letter() + Fore.LIGHTWHITE_EX
            + number.main_part.number_part()
            + Fore.LIGHTGREEN_EX + number.main_part.tail_letters() + Fore.RESET
            + '_' + str(number.region.code)
            + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
        )
    else:
        print(
            Fore.LIGHTWHITE_EX + number.main_part.first_letter() 
            + Fore.RESET + number.main_part.number_part() 
            + Fore.LIGHTWHITE_EX + number.main_part.tail_letters() 
            + Fore.RESET + '_' + str(number.region.code) 
            + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
        )

argsParser = argparse.ArgumentParser()
argsParser.add_argument(
    '-c', '--count',
    help="count of gos numbers generations. By default if 1",
    required=False,
    type=int,
    default=1
)

argsParser.add_argument(
    '-r', '--region-code',
    help="region code, generations only for this code",
    required=False,
)

argsParser.add_argument(
    '-p', '--pay-bribe',
    help='pay a bribe?',
    required=False,
    action='store_true'
)

args = argsParser.parse_args()

try:
    gibdd = Gibdd(args.region_code)
except Exception as e:
    print(e)
    exit()

numbers = sorted(
    [gibdd.create_number(args.pay_bribe) for i in range(args.count)], 
    key=lambda x: (x.region.name, x.main_part.to_str(), x.region.name)
)

for number in numbers:
    output_type(number)
