import random
import string


def hashed():
    let = string.ascii_uppercase + string.ascii_lowercase
    dig = string.digits
    hash = random.choices(let, k=1) + random.choices(let + dig, k=5)
    return "".join(hash)
