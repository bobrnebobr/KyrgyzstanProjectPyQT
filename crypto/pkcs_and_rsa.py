from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
import binascii


def generate_and_save_keys(passphrase):
    keyPair = RSA.generate(2048)

    with open('publicKey.pem', mode='wb') as f:
        f.write(keyPair.public_key().exportKey("PEM"))

    with open('privateKey.pem', mode='wb') as f:
        f.write(keyPair.exportKey('PEM', passphrase=passphrase))


def encrypt_key(key):
    with open('publicKey.pem') as f:
        public_key = RSA.importKey(f.read())
    encryptor = PKCS1_OAEP.new(public_key)
    encrypted = encryptor.encrypt(bytes(key, encoding='utf-8'))
    return encrypted


def decrypt_key(cipher_text, passphrase):
    with open('privateKey.pem') as f:
        private_key = RSA.importKey(f.read(), passphrase=passphrase)
    decryptor = PKCS1_OAEP.new(private_key)
    decrypted = decryptor.decrypt(cipher_text)
    return decrypted


def save_login_data(enc_key, hashed_master_password):
    with open('Login Data', mode='wb') as f:
        f.write(encrypt_key(enc_key))
    with open('Salt Data', mode='w') as f:
        f.write(hashed_master_password[-10:].decode())


def get_enc_key(password):
    with open('Login Data', 'rb') as f:
        encrypted_key = f.read()
    return decrypt_key(encrypted_key, password)


def get_salt():
    with open('Salt Data') as f:
        return f.read()
