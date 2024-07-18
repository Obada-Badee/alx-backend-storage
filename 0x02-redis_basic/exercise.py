#!/usr/bin/env python3
""" Redis Class Module """


import redis
from typing import Union,Any
import uuid


class Cache:
    """ Class that specify the cache opertion """

    def __init__(self) -> None:
        """Initilize the redis """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate a random key store the input data in Redis"""

        _id = str(uuid.uuid4())
        self._redis.set(_id, data)
        return _id
