import random

from crypto import aes_256_cgm_algorithm
from crypto import pkcs_and_rsa
from crypto import pbkdf2
import asyncio
import random


async def wait_random_time():
    await asyncio.sleep(random.randint(1, 1000) / 1000)


def create_login_data(master_password):
    asyncio.run(wait_random_time())
    hashed_master_password = pbkdf2.hash_message(master_password, pbkdf2.generate_salt().encode())
    pkcs_and_rsa.generate_and_save_keys(hashed_master_password)
    enc_key = aes_256_cgm_algorithm.generate_enc_key()
    pkcs_and_rsa.save_login_data(enc_key, hashed_master_password)


def encode_message(message, password):
    hashed_password_salt = pkcs_and_rsa.get_salt().encode()
    asyncio.run(wait_random_time())
    return aes_256_cgm_algorithm.encrypt_AES_GCM(message, pkcs_and_rsa.get_enc_key(pbkdf2.hash_message(password, hashed_password_salt)))


def decode_message(cipher_text, password):
    hashed_password_salt = pkcs_and_rsa.get_salt().encode()
    asyncio.run(wait_random_time())
    return aes_256_cgm_algorithm.decrypt_AES_GCM(cipher_text, pkcs_and_rsa.get_enc_key(pbkdf2.hash_message(password, hashed_password_salt))).decode()


def check_password(password):
    asyncio.run(wait_random_time())
    try:
        pkcs_and_rsa.get_enc_key(pbkdf2.hash_message(password, pkcs_and_rsa.get_salt().encode()))
        return True
    except Exception:
        return False
