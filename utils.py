import string
import random


def generate_password(count: int):
    symbols = {
        "D": string.digits,
        "L": string.ascii_lowercase,
        "P": string.punctuation,
        "U": string.ascii_uppercase
    }

    password = ''

    quote = list('D' * (count // 4) + 'U' * (count // 4) + 'P' * (count // 4) + 'L' * (count - 3 * (count // 4)))
    random.shuffle(quote)
    for i in quote:
        password += random.choice(list(symbols[i]))

    return password