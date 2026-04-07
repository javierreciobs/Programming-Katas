from flatten_array import flatten_array

def test_1():
    assert flatten_array([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_2():
    assert flatten_array([1, 2, 3]) == [1, 2, 3]

def test_3():
    assert flatten_array([]) == []