import hashlib
import random


POSSIBLE_SALT_SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,;:{}[]*#@'


def generate_salt():
    salt = ''
    for i in range(10):
        salt += random.choice(POSSIBLE_SALT_SYMBOLS)
    return salt


def hash_message(message, salt):
    return hashlib.pbkdf2_hmac('sha256', message.encode(), salt, 100000) + b'$$$' + salt
