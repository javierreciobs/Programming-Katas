from longest_word import longest_word
from longest_word import senior_longest_word

def test_returns_first_word_when_equal_lenghts():
    assert longest_word("hello world") == "hello"

def test_return_first_word_when_equal_lengths_2():
    assert longest_word("the quick brown fox") == "quick"

def test_return_python():
    assert longest_word("I love Python") == "Python"

def test_return_quotes_when_empty_input():
    assert longest_word("") == ""

def test_senior_1():
    assert senior_longest_word("hello world") == "hello"

def test_senior_2():
    assert senior_longest_word("the quick brown fox") == "quick"

def test_senior_3():
    assert senior_longest_word("I love Python") == "Python"

def test_senior_4():
    assert senior_longest_word("") == ""