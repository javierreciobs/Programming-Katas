from sudoku_row_validator import sudoku_row_validator

def test_return_true_when_sort_numbers():
    assert sudoku_row_validator([1, 2, 3, 4, 5, 6, 7, 8, 9]) == True

def test_return_true_when_unordered_numbers():
    assert sudoku_row_validator([9, 8, 7, 6, 5, 4, 3, 2, 1]) == True

def test_return_false_when_duplicates_numbers():
    assert sudoku_row_validator([1, 2, 3, 4, 5, 6, 7, 8, 8,]) == False

def test_return_false_when_zero_in_row():
    assert sudoku_row_validator([0, 2, 3, 4, 5, 6, 7, 8, 9]) == False

def test_return_false_when_lack_of_number():
    assert sudoku_row_validator([1, 2, 3, 4, 5, 6, 7, 8]) == False

def test_return_false_when_more_than_9_numbers():
    assert sudoku_row_validator([1, 2, 3, 4, 5, 6, 7, 8, 8, 9]) == False