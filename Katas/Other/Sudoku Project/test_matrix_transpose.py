from matrix_transpose import matrix_transpose
from matrix_transpose import senior_matrix_transpose 

def test_return_3_list_of_2_elements():
    assert matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_return_2_list_of_3_elements():
    assert matrix_transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

def test_return_2_list_of_2_elements():
    assert matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_return_list_when_empty_input():
    assert matrix_transpose([]) == []

def test_return_3_list_of_2_elements_with_senior():
    assert senior_matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_return_2_list_of_3_elements_with_senior():
    assert senior_matrix_transpose([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]

def test_return_2_list_of_2_elements_with_senior():
    assert senior_matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_return_list_when_empty_input_with_senior():
    assert senior_matrix_transpose([]) == []