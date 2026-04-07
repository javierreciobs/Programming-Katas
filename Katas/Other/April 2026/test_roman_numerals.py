from roman_numerals import to_roman

def test_return_1_in_roman():
    assert to_roman(1) == "I"

def test_return_4_in_roman():
    assert to_roman(4) == "IV"

def test_return_9_in_roman():
    assert to_roman(9) == "IX"

def test_return_14_in_roman():
    assert to_roman(14) == "XIV"

def test_return_40_in_roman():
    assert to_roman(40) == "XL"

def test_return_90_in_roman():
    assert to_roman(90) == "XC"

def test_return_400_in_roman():
    assert to_roman(400) == "CD"

def test_return_900_in_roman(): 
    assert to_roman(900) == "CM"

def test_return_1994_in_roman():
    assert to_roman(1994) == "MCMXCIV"

def test_return_2026_in_roman():
    assert to_roman(2026) == "MMXXVI"