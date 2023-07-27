#!/usr/bin/env python3
"""
a class BasicCache that inherits from BaseCaching
and is a caching system:
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Basic caching system implementing the MRU(Most recently Used)
    replacement policy

    """

    def __init__(self):
        super().__init__()
        self.order_list = list()
        self.put_count = -1

    def put(self, key, item):
        """
        assign the value of a key to the cache_data attribute if the
        parent class
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:
            key_to_del = self.order_list[self.put_count]
            print("DISCARD: {}".format(key_to_del))
            del self.cache_data[key_to_del]
            if key in self.order_list:
                self.order_list.remove(key)
            self.order_list.append(key)
        if key not in self.order_list:
            self.order_list.append(key)
        else:
            self.order_list.remove(key)
            self.order_list.append(key)

    def get(self, key):
        "get the value for a key from a cache"
        if key and key in self.cache_data.keys():
            self.order_list.remove(key)
            self.order_list.append(key)
            return self.cache_data[key]
        else:
            return None
