from sudoku_box_validator import sudoku_box_validator
from sudoku_box_validator import senior_sudoku_box_validator 

def test_return_true_when_all_conditions():
    assert sudoku_box_validator([[1,2,3],[4,5,6],[7,8,9]]) == True

def test_return_false_when_duplicates():
    assert sudoku_box_validator([[1,1,3],[4,5,6],[7,8,9]]) == False

def test_return_false_when_zero():
    assert sudoku_box_validator([[1,2,3],[4,5,6],[7,8,0]]) == False

def test_return_true_when_disordered_case_1():
    assert sudoku_box_validator([[3,1,2],[6,4,5],[9,7,8]]) == True

def test_return_true_when_disordered_case_2():
    assert sudoku_box_validator([[9,8,7],[6,5,4],[3,2,1]]) == True

def test_return_true_when_all_conditions_with_senior():
    assert senior_sudoku_box_validator([[1,2,3],[4,5,6],[7,8,9]]) == True

def test_return_false_when_duplicates_with_senior():
    assert senior_sudoku_box_validator([[1,1,3],[4,5,6],[7,8,9]]) == False

def test_return_false_when_zero_with_senior():
    assert senior_sudoku_box_validator([[1,2,3],[4,5,6],[7,8,0]]) == False

def test_return_true_when_disordered_case_1_with_senior():
    assert senior_sudoku_box_validator([[3,1,2],[6,4,5],[9,7,8]]) == True

def test_return_true_when_disordered_case_2_with_senior():
    assert senior_sudoku_box_validator([[9,8,7],[6,5,4],[3,2,1]]) == True


