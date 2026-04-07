from two_sum import two_sum

def test_first():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_second():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_thrid():
    assert two_sum([3, 3], 6) == [0, 1]
        