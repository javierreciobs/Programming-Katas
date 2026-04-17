from flatten_deep import flatten_deep
from flatten_deep import senior_flatten_deep

def test_standard_flatten_list():
    assert flatten_deep([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

def test_return_list_when_many_nested_list():
    assert flatten_deep([[1, [2]], [3, [4, [5]]]]) == [1, 2, 3, 4, 5]

def test_return_list_when_empty_input():
    assert flatten_deep([]) == []

def test_return_list_when_one_list_input():
    assert flatten_deep([1, 2, 3]) == [1, 2, 3]

def test_senior_standard_flatten_list():
    assert senior_flatten_deep([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

