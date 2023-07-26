#!/usr/bin/env python3
"""
a class BasicCache that inherits from BaseCaching
and is a caching system:
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Basic caching system
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        assign the value of a key to the cache_data attribute if the
        parent class
        """
        if item and key:
            self.cache_data[key] = item
            if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                self.cache_data.pop(first_key)
                print("DISCARD {}".format(first_key))

    def get(self, key):
        "get the value for a key from a cache"
        if key and key in self.cache_data.keys():
            return self.cache_data[key]
