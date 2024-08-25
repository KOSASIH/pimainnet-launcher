import hashlib
import hmac
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.primitives import serialization

class Encryptor:
    def __init__(self, key, cipher_type, mode, padding_type):
        self.key = key
        self.cipher_type = cipher_type
        self.mode = mode
        self.padding_type = padding_type
        self.cipher = self._get_cipher()

    def _get_cipher(self):
        if self.cipher_type == 'AES':
            return Cipher(algorithms.AES(self.key), self.mode, backend=default_backend())
        elif self.cipher_type == 'RSA':
            return rsa.RSAPrivateKey.from_private_bytes(self.key, password=None)
        else:
            raise ValueError('Invalid cipher type')

    def encrypt(self, plaintext):
        if self.cipher_type == 'AES':
            encryptor = self.cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(plaintext) + padder.finalize()
            return encryptor.update(padded_data) + encryptor.finalize()
        elif self.cipher_type == 'RSA':
            return self.cipher.encrypt(
                plaintext,
                asymmetric_padding.OAEP(
                    mgf=asymmetric_padding.MGF1(algorithm=hashlib.SHA256()),
                    algorithm=hashlib.SHA256(),
                    label=None
                )
            )
        else:
            raise ValueError('Invalid cipher type')

    def decrypt(self, ciphertext):
        if self.cipher_type == 'AES':
            decryptor = self.cipher.decryptor()
            decrypted_padded_data = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            return unpadder.update(decrypted_padded_data) + unpadder.finalize()
        elif self.cipher_type == 'RSA':
            return self.cipher.decrypt(
                ciphertext,
                asymmetric_padding.OAEP(
                    mgf=asymmetric_padding.MGF1(algorithm=hashlib.SHA256()),
                    algorithm=hashlib.SHA256(),
                    label=None
                )
            )
        else:
            raise ValueError('Invalid cipher type')

class AESEncryptor(Encryptor):
    def __init__(self, key, mode, padding_type):
        super().__init__(key, 'AES', mode, padding_type)

class RSAEncryptor(Encryptor):
    def __init__(self, key, padding_type):
        super().__init__(key, 'RSA', None, padding_type)

class HMACSigner:
    def __init__(self, key):
        self.key = key

    def sign(self, message):
        return hmac.new(self.key, message, hashlib.SHA256).digest()

    def verify(self, message, signature):
        expected_signature = hmac.new(self.key, message, hashlib.SHA256).digest()
        return hmac.compare_digest(expected_signature, signature)
