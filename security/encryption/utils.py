import os
import base64

def generate_key(key_size):
    return os.urandom(key_size)

def serialize_key(key):
    return key.decode('latin-1')

def deserialize_key(serialized_key):
    return serialized_key.encode('latin-1')

def encode_base64(data):
    return base64.b64encode(data).decode('utf-8')

def decode_base64(encoded_data):
    return base64.b64decode(encoded_data.encode('utf-8'))
