#!/usr/bin/env python3
""" Redis Class Module """


import redis
from typing import Union, Any, Callable, TypeVar
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

    def get(self, key: str,
            fn: Union[Callable[[T], T], None]) -> Union[T, None]:
        """ Reading from Redis and recovering original type """

        _value = self._redis.get(key)
        if not _value:
            return None
        else:
            if fn:
                _vlaue = fn(_vlaue)

        return _vlaue

    def get_str(self, key: str) -> Union[str, None]:
        """ automatically parametrize Cache.get with str """

        _value = self._redis.get(key)
        if not _value:
            return None
        else:
            return lambda _vlaue: _vlaue.decode("utf-8")

    def get_int(self, key: str) -> Union[int, None]:
        """ automatically parametrize Cache.get with int """

        _value = self._redis.get(key)
        if not _value:
            return None
        else:
            return int(_value)
