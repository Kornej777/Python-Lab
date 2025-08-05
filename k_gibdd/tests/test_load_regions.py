from k_gibdd import *

def test_load_from_www():
    r = Regions.from_internet()
    assert len(r.regions_codes()) == 141

def test_load_from_dict():
    r = Regions.from_internet('https://www.sibtyre.ru/catalog/letnyaya/')
    assert len(r.regions_codes()) == 141

def test_data_is_identical():
    r = Regions.from_internet('https://chat.deepseek.com/a/chat/s/657c7478-56ce-4cd4-b14b-90c28112c467')
    r2 = Regions.from_internet()
    assert r.regions_codes() == r2.regions_codes()
    moscow_region = r.actual_region('99')
    assert moscow_region.code == '799'
    assert moscow_region.name == 'Москва'

def test_invalid():
    r = Regions.from_internet('https://www.sibtyre.root777')
    assert len(r.regions_codes()) == 141






