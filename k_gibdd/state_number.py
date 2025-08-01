from k_gibdd.region import Regions
import exrex
import random
from enum import Enum
import re

class StateNumberType(Enum):
    SUPER_COOL = 1
    COOL_DIGITS = 2
    COOL_LETTERS = 3
    REGULAR = 4

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
        if self.code != None and self.code not in self.regions.regions_codes():
            raise Exception(f'Регион {self.code} не найден.')

    def create_number(self, bribe):
        
        if bribe:
            letters = random.choice([
            random.choice(self._cool_letters()),
            self._random_letters()
            ])
            digits = random.choice([
                random.choice(self._cool_digits()),
                self._random_digits()
            ])
        else:
            letters = self._random_letters()
            digits = self._random_digits()

        main_part = StateNumberMainPart(letters, digits)

        if self.code is not None:
            region = self.regions.for_region(self.code)
        else:
            region = self.regions.random()

        return StateNumber(main_part, region)
    
    def is_number_valid(self, number):
        if re.match(r'^[АВЕКМНОРСТУХABEKMNOPCTYX]{1}\d{3}[АВЕКМНОРСТУХABEKMNOPCTYX]{2}_\d{2,3}$', number.upper()):
            return True
    def user_number(self, number):
        letters = [number[0], number[4], number[5]]
        digits = [number[1], number[2], number[3]]
        main_part = StateNumberMainPart(letters, digits)
        region = self.regions.for_region(number[7:])
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
            cool_digits.append([i, i, i])

            if i <= 7:
                cool_digits.append([i, i + 1, i + 2])
            if i >= 2:
                cool_digits.append([i - 2, i - 1, i])

        return cool_digits
    
    def _cool_letters(self):
        cool_letters = [
        ['А', 'М', 'Р'],
        ['Е', 'К', 'Х'],
        ['Х', 'К', 'Х'],
        ['О', 'О', 'О'],
        ['Р', 'М', 'Р'],
        ['У', 'М', 'Р'],
        ['В', 'О', 'О'],
        ['А', 'О', 'О'],
        ['С', 'А', 'С'],
        ['М', 'О', 'С'],
        ['А', 'К', 'Р'],
        ['Е', 'Р', 'Е'],
        ['А', 'Н', 'А'],
    ]
        for l in 'АВЕКМНОРСТУХ':
            cool_letters.append([l, l, l])
        return cool_letters
    
    def number_type(self, number):

        digits = [int(d) for d in number.main_part.number_part()]
        letters = list(number.main_part.first_letter() + number.main_part.tail_letters())

        if digits in self._cool_digits() and letters in self._cool_letters():
            return StateNumberType.SUPER_COOL
        elif digits in self._cool_digits():
            return StateNumberType.COOL_DIGITS
        elif letters in self._cool_letters():
            return StateNumberType.COOL_LETTERS
        else:
            return StateNumberType.REGULAR