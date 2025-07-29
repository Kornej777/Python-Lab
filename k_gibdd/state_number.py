from k_gibdd.region import Regions
import exrex

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
    def __init__(self):
        self.regions = Regions()

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
        main_part = StateNumberMainPart(self._random_letters(), self._random_digits())
        region = self.regions.random()
        return StateNumber(main_part, region)


