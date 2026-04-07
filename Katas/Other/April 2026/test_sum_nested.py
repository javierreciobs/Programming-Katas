from sum_nested import sum_nested

def test_return_total_sum_when_more_than_an_array():
    assert sum_nested([1, [2, 3], [4, [5, 6]]]) == 21

def test_return_total_sum_from_array():
    assert sum_nested([1, 2, 3]) == 6

def test_return_zero_when_empty_input():
    assert sum_nested([]) == 0

def test_return_number_when_more_than_an_array():
    assert sum_nested([[[[5]]]]) == 5