import random
import string


def get_random_password(how_long=8) -> str:
    lettersh = string.ascii_uppercase
    lettersl = string.ascii_lowercase
    nombers = string.digits
    list_simbols = lettersl + lettersh + nombers
    password = random.sample(list_simbols, how_long)
    return ''.join(password)


print(get_random_password())
