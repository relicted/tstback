import uuid
import hashlib


def hash_password(password):
    salt = uuid.uuid4().hex
    hashed_password = hashlib.sha512(f'{salt}{password}'.encode('utf-8')).hexdigest()
    return salt, hashed_password


def get_hashed_password(salt, password):
    hashed_password = hashlib.sha512(f'{salt}{password}'.encode('utf-8')).hexdigest()
    return hashed_password