import random
import string


def get_magic_str():
    str_plus_nums = string.ascii_letters + string.digits
    return ''.join((random.choice(str_plus_nums) for x in range(6)))
