from k_gibdd.region import Regions
import exrex
import random

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
    def __init__(self, code = None, bribe = 'n'):
        self.regions = Regions()
        self.code = code
        self.bribe = bribe
        if self.code == None:
            pass
        elif self.code not in self.regions.regions_codes():
            raise Exception(f'Регион {self.code} не найден.')

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

    def create_number(self):
        cool_digits = [
    [0, 0, 1],
    [0, 0, 7],
    [1, 2, 3],
    [7, 7, 7],
    [1, 0, 0],
    [5, 0, 0],
    [9, 9, 9],
    [0, 0, 0],
    [1, 7, 7],
    [7, 0, 7],
    [2, 3, 4],
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4],
    [5, 5, 5],
    [6, 6, 6],
    [8, 8, 8],
    [1, 1, 1],
    [6, 7, 8],
    [7, 7, 1] 
]
        cool_letters = [
    "ААА",
    "АМР",
    "ЕКХ",
    "ХКХ",
    "ООО",
    "ССС",
    "МММ",
    "РМР",
    "УМР",
    "ВОО",
    "ТТТ",
    "ККК",
    "АОО",
    "САС",
    "МОС",
    "ХХХ",
    "АКР",
    "ЕРЕ",
    "АНА",
    "УУУ" 
]
        if self.bribe == 'n':
            main_part = StateNumberMainPart(self._random_letters(), self._random_digits())
            if self.code:
                region = self.regions.for_region(self.code)
                return StateNumber(main_part, region)
            else:
                region = self.regions.random()
                return StateNumber(main_part, region)
        else:
            main_part = StateNumberMainPart(random.choice(cool_letters), random.choice(cool_digits))
            if self.code:
                region = self.regions.for_region(self.code)
                return StateNumber(main_part, region)
            else:
                region = self.regions.random()
                return StateNumber(main_part, region)


