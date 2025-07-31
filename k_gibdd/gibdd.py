import argparse
from k_gibdd.state_number import Gibdd
from colorama import Fore, init
init(autoreset = True)

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
    action='store_true',
    default=False
)

args = argsParser.parse_args()

try:
    gibdd = Gibdd(args.region_code, args.pay_bribe)
except Exception as e:
    print(e)
    exit()

numbers = sorted(
    [gibdd.create_number() for i in range(int(args.count))], 
    key=lambda x: (x.region.name, x.main_part.to_str(), x.region.name)
)

for number in numbers:
    print(Fore.LIGHTWHITE_EX + number.main_part.first_letter() 
          + Fore.RESET + number.main_part.number_part() 
          + Fore.LIGHTWHITE_EX + number.main_part.tail_letters() 
          + Fore.RESET + '_' + str(number.region.code) + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET)
