from sudoku_box_generator import sudoku_box_generator

def test_returns_three_rows_for_grid():
    result = sudoku_box_generator()
    assert len(result) == 3

def test_returns_three_columns_per_row():
    result = sudoku_box_generator()
    assert len(result[0]) == 3

def test_contains_all_numbers_from_one_to_nine():
    result = sudoku_box_generator()
    flat_list = [n for row in result for n in row]
    assert set(flat_list) == set(range(1, 10))

def test_generates_different_boxes_each_time():
    box_1 = sudoku_box_generator()
    box_2 = sudoku_box_generator()
    assert box_1 != box_2