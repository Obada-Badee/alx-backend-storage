#!/usr/bin/env python3
""" Redis Class Module """


import redis
from typing import Union, Callable, TypeVar
import uuid


T = TypeVar('T', int, float, bytes, str)


class Cache:
    """ Class that specify the cache opertion """

    def __init__(self) -> None:
        """Initilize the redis """

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: T) -> str:
        """generate a random key store the input data in Redis"""

        _id = str(uuid.uuid4())
        self._redis.set(_id, data)
        return _id

    def get(self, key: str, fn: Callable = None) -> T:
        """ Reading from Redis and recovering original type """

        _value = self._redis.get(key)
        if fn:
            _value = fn(_value)
        return _value

    def get_str(self, key: str) -> Union[str, None]:
        """ automatically parametrize Cache.get with str """

        _value = self._redis.get(key, str).decode("utf-8")
        return _value

    def get_int(self, key: str) -> int:
        """ automatically parametrize Cache.get with int """

        _value = self._redis.get(key, int)
        return _value
