# KATA: DNI Letter
#
# Dado un número de DNI, calcula la letra que le corresponde.
#
# TABLA: "TRWAGMYFPDXBNJZSQVHLCKE"
#
# dni_letter(12345678) == "Z"
# dni_letter(00000000) == "T"
# dni_letter(99999999) == "R"
# dni_letter(12345670) == "M"

LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"

def dni_letter(dni_number):
    letter_index = dni_number % 23
    letter = LETTERS[letter_index]
    return letter

#Senior

def senior_dni_letter(senior_dni_number):
    return LETTERS[senior_dni_number % 23]
