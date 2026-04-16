from chunk_array import chunk_array
from chunk_array import senior_chunk_array

def test_return_list_of_2_elements_and__one_list_of_one_element():
    assert chunk_array([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

def test_return_list_of_3_elements():
    assert chunk_array([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]

def test_return_list_when_empty_input():
    assert chunk_array([], 3) == []

def test_return_list_of_one_element():
    assert chunk_array([1, 2, 3], 1) == [[1], [2], [3]]

def test_senior_return_list_of_2_elements_and_one_list_of_one_element():
    assert senior_chunk_array([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]