from unique_ordered import unique_ordered
from unique_ordered import senior_unique_ordered 

def test_with_numbers():
    assert unique_ordered([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

def test_with_letters():
    assert unique_ordered(["a", "b", "a", "c"]) == ["a", "b", "c"]

def test_return_list_when_empty_input():
    assert unique_ordered([]) == []

def test_with_numbers_with_senior():
    assert senior_unique_ordered([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]

def test_with_letters_with_senior():
    assert senior_unique_ordered(["a", "b", "a", "c"]) == ["a", "b", "c"]

def test_return_list_when_empty_input_with_senior():
    assert senior_unique_ordered([]) == []
