from Cryptodome.Cipher import AES
import hashlib
import os
import binascii
import random


def encrypt_AES_GCM(msg, password):
    kdfSalt = os.urandom(16)
    secretKey = hashlib.scrypt(password, salt=kdfSalt, n=16384, r=8, p=1, dklen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM)
    ciphertext, authTag = aesCipher.encrypt_and_digest(msg.encode())
    return (kdfSalt, ciphertext, aesCipher.nonce, authTag)


def decrypt_AES_GCM(encryptedMsg, password):
    (kdfSalt, ciphertext, nonce, authTag) = encryptedMsg
    secretKey = hashlib.scrypt(password, salt=kdfSalt, n=16384, r=8, p=1, dklen=32)
    aesCipher = AES.new(secretKey, AES.MODE_GCM, nonce)
    plaintext = aesCipher.decrypt_and_verify(ciphertext, authTag)
    return plaintext


def generate_enc_key():
    return str(random.randint(0, 2 ** 256))


if __name__ == "__main__":
    print(generate_enc_key())
