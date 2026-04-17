from sort_by_length import sort_by_length
from sort_by_length import senior_sort_by_length

def test_return_list_when_letters_input():
    assert sort_by_length(["a", "ccc", "dd", "bb"]) == ["a", "dd", "bb", "ccc"]

def test_return_list_when_words_input():
    assert sort_by_length(["apple", "pie", "shortcake"]) == ["pie", "apple", "shortcake"]

def test_return_emtpy_list_when_empty_input():
    assert sort_by_length([]) == []

def test_senior_return_list_when_letter_input():
    assert senior_sort_by_length(["a", "ccc", "dd", "bb"]) == ["a", "dd", "bb", "ccc"]

def test_senior_return_list_when_words_input():
    assert senior_sort_by_length(["apple", "pie", "shortcake"]) == ["pie", "apple", "shortcake"]