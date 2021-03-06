import re

def is_valid_email(email):
    EMAIL_REGEX = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
    return re.match(EMAIL_REGEX, email)

def is_valid_password(password):
    PASSWORD_REGEX = "^(?=.*[a-zA-Z])(?=.*[!@#$%^~*+=-])(?=.*[0-9]).{8,}$"
    return re.match(PASSWORD_REGEX, password)