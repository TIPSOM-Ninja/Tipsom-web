from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
import base64
from django.conf import settings

def decrypt_data(encrypted_data):
    with open(settings.PRIVATE_KEY, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    
    decrypted = private_key.decrypt(
        base64.b64decode(base64.b64decode(encrypted_data)),
        padding.PKCS1v15()
    ).decode('utf-8')
    print(decrypted)
    return decrypted
