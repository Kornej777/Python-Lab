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
    action='store_true'
)

args = argsParser.parse_args()

try:
    gibdd = Gibdd(args.region_code)
except Exception as e:
    print(e)
    exit()

numbers = sorted(
    [gibdd.create_number(args.pay_bribe) for i in range(int(args.count))], 
    key=lambda x: (x.region.name, x.main_part.to_str(), x.region.name)
)

for number in numbers:
    print(gibdd._is_valid(number))
