from k_gibdd import *

gibdd = Gibdd()

def test_state_number():
    assert StateNumber(
        StateNumberMainPart(['A', 'A', 'A'], [3, 4, 2]), 
        Region('90', "region name")
    ).to_str() == "A342AA_90"

def test_number_check():
    assert RawStateNumber('А123АА_77').is_valid()

def test_number_check2():
    assert RawStateNumber('b123aa_77').is_valid()

def test_number_check3():
    n ='y113Аk_777'
    assert RawStateNumber(n).to_string()








