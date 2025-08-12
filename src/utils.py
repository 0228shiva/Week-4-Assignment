def validate_airport_code(code):
    return isinstance(code, str) and len(code) == 3 and code.isalpha()
