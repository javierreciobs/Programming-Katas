from count_duplicates import count_duplicates

def test_1():
    assert count_duplicates("aabbcc") == 3

def test_2():
    assert count_duplicates("aabbb") == 2

def test_3():
    assert count_duplicates("hello") == 1

def test_4():
    assert count_duplicates("abcd") == 0

def test_5():
    assert count_duplicates("") == 0