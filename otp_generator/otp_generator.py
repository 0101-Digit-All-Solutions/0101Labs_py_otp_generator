import random
import string

def generate_otp(length=6, numeric=True, alphabets=False, special_chars=False):
    if length <= 0:
        raise ValueError("Length must be a positive integer.")

    char_set = ''
    if numeric:
        char_set += string.digits
    if alphabets:
        char_set += string.ascii_letters
    if special_chars:
        char_set += string.punctuation

    if not char_set:
        raise ValueError("At least one option must be True.")

    return ''.join(random.choices(char_set, k=length))
