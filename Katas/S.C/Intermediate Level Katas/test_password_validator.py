from password_validator import password_validator

def test_password_with_all_conditions():
    assert password_validator("1234abcdABCD_") == True

def test_password_with_enough_lenght():
    assert password_validator("1aA_") == False

def test_password_without_number():
    assert password_validator("abcdABCD_") == False

def test_password_without_lower_case():
    assert password_validator("1234ABCD_") == False

def test_password_without_upper_case():
    assert password_validator("1234abcd_") == False

def test_password_without_underscore():
    assert password_validator("1234abcdABCD") == False