import os
from pymongo import errors


class BaseModel(object):
    DuplicateKeyError = errors.DuplicateKeyError

    def __init__(self, request, db=None, collection=None, **kwargs):
        self._db = request.app.mongo[db or os.getenv('DEFAULT_DATABASE')]
        if collection:
            self._collection = collection
