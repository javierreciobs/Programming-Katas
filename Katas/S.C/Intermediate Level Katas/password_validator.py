#Password Validator

#isdigit allows to test if string has numbers, instead of "1" in, "2" in, etc


def password_validator(string):
        return(
        len(string) >= 6 
        and any(c.isdigit() for c in string) 
        and any(c.islower() for c in string) 
        and any(c.isupper() for c in string) 
        and "_" in string)
        