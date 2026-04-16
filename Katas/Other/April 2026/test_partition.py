from partition import partition
from partition import senior_partition

def test_return_standard_numbers_partition():
    assert partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0) == ([2, 4], [1, 3, 5])

def test_return_standard_words_partition():
    assert partition(["hi", "hello", "hey"], lambda s: len(s) > 2) == (["hello", "hey"], ["hi"])

def test_return_empty_partition_lists_when_empty_input():
    assert partition([], lambda x: x > 0) == ([], [])

def test_return_empty_condition_list():
    assert partition([1, 2, 3], lambda x: x > 10) == ([], [1, 2, 3])

def test_senior_standard_partitino():
    assert senior_partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0) == ([2, 4], [1, 3, 5])
