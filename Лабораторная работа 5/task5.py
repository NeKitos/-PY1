import random
import string


def get_random_password() -> str:
    lettersh = string.ascii_uppercase
    lettersl = string.ascii_lowercase
    nombers = string.digits
    list_simbols = lettersl + lettersh + nombers
    password = random.sample(list_simbols, 8)
    return ''.join(password)

print(get_random_password())
