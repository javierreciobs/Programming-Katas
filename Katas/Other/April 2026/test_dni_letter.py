from dni_letter import dni_letter
from dni_letter import senior_dni_letter 

def test_return_letter_Z():
    assert dni_letter(12345678) == "Z"

def test_return_letter_T():
    assert dni_letter(00000000) == "T"

def test_return_letter_R():
    assert dni_letter(99999999) == "R"

def test_return_letter_M():
    assert dni_letter(12345670) == "Y"

def test_return_letter_Z_with_senior():
    assert senior_dni_letter(12345678) == "Z"

def test_return_letter_T_with_senior():
    assert senior_dni_letter(00000000) == "T"

def test_return_letter_R_with_senior():
    assert senior_dni_letter(99999999) == "R"

def test_return_letter_M_with_senior():
    assert senior_dni_letter(12345670) == "Y"