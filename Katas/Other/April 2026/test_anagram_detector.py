from anagram_detector import anagram_detector

def test_return_true_when_one_word_anagram():
    assert anagram_detector("listen", "silent") == True

def test_return_false_when_not_anagram():
    assert anagram_detector("hello", "world") == False

def test_return_true_when_2_words_anagram():
    assert anagram_detector("Astronomer", "Moon starer") == True

def test_return_true_when_empty_anagram():
    assert anagram_detector("", "")  == True