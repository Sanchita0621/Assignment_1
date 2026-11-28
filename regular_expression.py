import re

def is_allowed_string(text):
    # ^[a-zA-Z0-9]+$ matches a non-empty string with only a-z, A-Z, 0-9
    pattern = r'^[a-zA-Z0-9]+$'
    return bool(re.match(pattern, text))

# Test cases
print(is_allowed_string("HelloWorld123"))  # True
print(is_allowed_string("Hello_World!"))   # False
print(is_allowed_string("Hello 123"))      # False (contains space)
