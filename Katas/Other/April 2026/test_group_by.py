from group_by import group_by
from group_by import senior_group_by

def test_return_rest_of_division_in_dic():
    assert group_by([1, 2, 3, 4, 5], lambda x: x % 2) == {0: [2, 4], 1: [1, 3, 5]}

def test_return_len_dic():
    assert group_by(["hi", "hello", "hey"], lambda s: len(s)) == {2: ["hi"], 5: ["hello"], 3: ["hey"]}

def test_return_dic_when_empty_iput():
    assert group_by([], lambda x: x) == {}

def test_return_impar_and_par_dic():
    assert group_by([1, 2, 3], lambda x: "par" if x % 2 == 0 else "impar") == {"impar": [1, 3], "par": [2]}

def test_return_dic_with_senior():
    assert senior_group_by([1, 2, 3, 4, 5], lambda x: x % 2) == {0: [2, 4], 1: [1, 3, 5]}