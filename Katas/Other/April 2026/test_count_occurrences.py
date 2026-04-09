from count_occurrences import count_occurrences
from count_occurrences import senior_count_occurences

def test_return_ocurrences_in_hello_world_hello():
    assert count_occurrences("hello world hello") == {"hello": 2, "world": 1}

def test_return_ocurrences_in_cat_example():
    assert count_occurrences("the cat sat on the mat") == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

def test_return_dic_when_empty_input():
    assert count_occurrences("") == {}

def test_senior_version_with_hello_world_example():
    assert senior_count_occurences("hello world hello") == {"hello": 2, "world": 1}

def test_senior_version_with_cat_example():
    assert senior_count_occurences("the cat sat on the mat") == {"the": 2, "cat": 1, "sat": 1, "on": 1, "mat": 1}

def test_senior_version_when_empty_input():
    assert senior_count_occurences("") == {}



