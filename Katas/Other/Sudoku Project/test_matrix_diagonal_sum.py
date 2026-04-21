from matrix_diagonal_sum import matrix_diagonal_sum
from matrix_diagonal_sum import senior_matrix_diagonal_sum 

def test_with_three_lists():
    assert matrix_diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15

def test_with_two_lists():
    assert matrix_diagonal_sum([[1, 0], [0, 1]]) == 2

def test_return_number_when_one_list_input():
    assert matrix_diagonal_sum([[5]]) == 5

def test_return_zero_when_empty_input():
    assert matrix_diagonal_sum([]) == 0

def test_with_three_lists_with_senior():
    assert senior_matrix_diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 15

def test_with_two_lists_with_senior():
    assert senior_matrix_diagonal_sum([[1, 0], [0, 1]]) == 2

def test_return_number_when_one_list_input_with_senior():
    assert senior_matrix_diagonal_sum([[5]]) == 5

def test_return_zero_when_empty_input_with_senior():
    assert senior_matrix_diagonal_sum([]) == 0