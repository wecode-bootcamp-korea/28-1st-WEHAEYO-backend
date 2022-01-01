import re

def is_email_valid(email):
    EMAIL_REGEX = "^[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+$"
    return re.match(EMAIL_REGEX, email)

def is_password_valid(password):
    PASSWORD_REGEX = "^(?=.*[a-zA-Z])(?=.*[!@#$%^~*+=-])(?=.*[0-9]).{8,}$"
    return re.match(PASSWORD_REGEX, password)