from find_path import find_path

def test():
    assert find_path([3, 1, 4, 2], lambda x: x > 3) == 4

def test():
    assert find_path([3, 1, 4, 2], lambda x: x > 10) == None