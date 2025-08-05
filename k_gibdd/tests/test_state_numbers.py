from k_gibdd import *

gibdd = Gibdd()

def test_state_number():
    assert StateNumber(
        StateNumberMainPart(['A', 'A', 'A'], [3, 4, 2]), 
        Region('90', "region name")
    ).to_str() == "A342AA_90"

def test_number_check():
    raw = RawStateNumber('А123АА_77')
    assert raw.is_valid()
    assert raw.to_number().region == '77'
    assert raw.to_number().main_part.number_part() == '123'
    
def test_number_check2():
    raw = RawStateNumber('b123aa_77')
    assert raw.is_valid()
    assert raw.to_number().region == '77'
    assert raw.to_number().main_part.number_part() == '123'


def test_number_check4():
    assert not RawStateNumber('b123a2a_77').is_valid()

def test_number_check5():
    n = Gibdd().create_number(False)
    assert n.region.code == Regions.from_internet().actual_region(n.region.code).code












