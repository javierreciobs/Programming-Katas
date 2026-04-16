from zip_list import zip_list
from zip_list import senior_zip_list

def test_return_standard_zip_list():
    assert zip_list([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")]

def test_return_zip_list_without_remaining_element():
    assert zip_list([1, 2], ["a", "b", "c"]) == [(1, "a"), (2, "b")]

def test_return_brackets_when_empty_first_list():
    assert zip_list([], ["a", "b"]) == []

def test_return_brackets_when_empty_second_list():
    assert zip_list([1, 2, 3], []) == []

def test_senior_function_with_standard_zip_list():
    assert senior_zip_list([1, 2, 3], ["a", "b", "c"]) == [(1, "a"), (2, "b"), (3, "c")]