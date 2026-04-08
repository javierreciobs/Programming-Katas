from capitalize_word import capitalize_word
from capitalize_word import senior_capitalize_word

def test_return_hello_world_in_capitalize():
    assert capitalize_word("hello world") == "Hello World"

def test_return_the_quick_brown_fox_in_capitalize():
    assert capitalize_word("the quick brown fox") == "The Quick Brown Fox"

def test_return_python_is_fun_in_capitalize():
    assert capitalize_word("python is fun") == "Python Is Fun"

def test_return_quotes_when_empty_input():
    assert capitalize_word("") == ""

def test_return_hello_world_in_capitalize_with_senior_capitalize_words():
    assert senior_capitalize_word("hello world") == "Hello World"

def test_return_the_quick_brown_fox_in_capitalize_with_senior_capitalize_word():
    assert senior_capitalize_word("the quick brown fox") == "The Quick Brown Fox"

def test_return_python_is_fun_in_capitalize_with_senior_capitalize_word():
    assert senior_capitalize_word("python is fun") == "Python Is Fun"

def test_return_quotes_when_empty_input_with_senior_capitalize_word():
    assert senior_capitalize_word("") == ""

