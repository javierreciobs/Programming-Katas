from decimal_to_binary import to_binary

def test_return_1_in_binary():
    assert to_binary(1) == "1"

def test_return_2_in_binary():
    assert to_binary(2) == "10"

def test_return_5_in_binary():
    assert to_binary(5) == "101"   

def test_return_10_in_binary():
    assert to_binary(10) == "1010"

def test_return_255_in_binary():
    assert to_binary(255) == "11111111"