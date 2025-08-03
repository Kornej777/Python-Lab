from k_gibdd import *

gibdd = Gibdd()

def test_state_number():
    assert StateNumber(
        StateNumberMainPart(['A', 'A', 'A'], [3, 4, 2]), 
        Region('90', "region name")
    ).to_str() == "A342AA_90"

def test_number_check():
    assert gibdd.is_number_valid('А123АА_77')

def test_number_check2():
    assert gibdd.is_number_valid('b123aa_77')

def test_number_check3():
    assert gibdd.is_number_valid('y113Аk_777')


