from k_gibdd.region import Regions
import exrex
import random
from colorama import Fore, init
init(autoreset = True)

class StateNumberMainPart:
    def __init__(self, letters, digits):
        self.letters = letters
        self.digits = digits

    def first_letter(self):
        return self.letters[0]

    def number_part(self):
        return ''.join([str(x) for x in self.digits])

    def tail_letters(self):
        return self.letters[1] + self.letters[2]
    
    def to_str(self):
        return self.first_letter() + self.number_part() + self.tail_letters()
    
class StateNumber:
    def __init__(self, main_part, region):
        self.main_part = main_part
        self.region = region

    def __repr__(self):
        return self.to_str()

    def to_str(self):
        return self.main_part.to_str() + '_' + self.region.code

class Gibdd:
    def __init__(self, code = None):
        self.regions = Regions()
        self.code = code
        if self.code == None:
            pass
        elif self.code not in self.regions.regions_codes():
            raise Exception(f'Регион {self.code} не найден.')

    def create_number(self, bribe):
        self.bribe = bribe
        
        if not self.bribe:
            letters = self._random_letters()
            digits = self._random_digits()
        else:
            letters = random.choice([
            random.choice(self._cool_letters()),
            self._random_letters()
        ])
        
            digits = random.choice([
                random.choice(self._cool_digits()),
                self._random_digits()
            ])

        main_part = StateNumberMainPart(letters, digits)

        if self.code is not None:
            region = self.regions.for_region(self.code)
        else:
            region = self.regions.random()

        return StateNumber(main_part, region)

    def _random_digits(self):
        digits = []
        for i in range(3):
            digits.append(exrex.getone(r'^\d$'))
        return digits
    
    def _random_letters(self):
        letters = []
        for i in range(3):
            letters.append(exrex.getone(r'^[АВЕКМНОРСТУХ]{1}$'))
        return letters
    
    def _cool_digits(self):
        cool_digits = []
        for i in range(0,10):
            cool_digits.append([i, 0, i])
            cool_digits.append([0, i, 0])
            cool_digits.append([0, 0, i])
            cool_digits.append([i, 0, 0])
            if i <= 7:
                cool_digits.append([i, i+1, i+2])
        return cool_digits
    
    def _cool_letters(self):
        return [
        ['А', 'А', 'А'],
        ['А', 'М', 'Р'],
        ['Е', 'К', 'Х'],
        ['Х', 'К', 'Х'],
        ['О', 'О', 'О'],
        ['С', 'С', 'С'],
        ['М', 'М', 'М'],
        ['Р', 'М', 'Р'],
        ['У', 'М', 'Р'],
        ['В', 'О', 'О'],
        ['Т', 'Т', 'Т'],
        ['К', 'К', 'К'],
        ['А', 'О', 'О'],
        ['С', 'А', 'С'],
        ['М', 'О', 'С'],
        ['Х', 'Х', 'Х'],
        ['А', 'К', 'Р'],
        ['Е', 'Р', 'Е'],
        ['А', 'Н', 'А'],
        ['У', 'У', 'У']
    ]
    

    def _is_valid(self, number):
        digits = [int(d) for d in number.main_part.number_part()]
        letters = list(number.main_part.first_letter() + number.main_part.tail_letters())
        if digits in self._cool_digits() and letters in self._cool_letters():
            return (
                Fore.LIGHTGREEN_EX + number.main_part.first_letter()
                + number.main_part.number_part()
                + number.main_part.tail_letters()
                + '_' + str(number.region.code)
                + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
            )
        if digits in self._cool_digits():
            return (
                Fore.LIGHTWHITE_EX + number.main_part.first_letter()
                + Fore.RED + number.main_part.number_part() + Fore.LIGHTWHITE_EX
                + number.main_part.tail_letters() + Fore.RESET
                + '_' + str(number.region.code)
                + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
            )
        elif letters in self._cool_letters():
            return (
                Fore.RED + number.main_part.first_letter() + Fore.LIGHTWHITE_EX
                + number.main_part.number_part()
                + Fore.RED + number.main_part.tail_letters() + Fore.RESET
                + '_' + str(number.region.code)
                + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
            )
        else:
            return (
                Fore.LIGHTWHITE_EX + number.main_part.first_letter() 
                + Fore.RESET + number.main_part.number_part() 
                + Fore.LIGHTWHITE_EX + number.main_part.tail_letters() 
                + Fore.RESET + '_' + str(number.region.code) 
                + Fore.LIGHTBLACK_EX + " (" + number.region.name + ")" + Fore.RESET
            )