#!/usr/bin/env python3
""" Task 1. Module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Comment """
    def __init__(self):
        """Initialize derived class with the parent class init method
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assign to the dictionary self.cache_data the item
        value for the key `key`
        """
        if key is None or item is None:
            pass
        else:
            length = len(self.cache_data)
            if length >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                print("DISCARD: {}".format(self.order[0]))
                del self.cache_data[self.order[0]]
                del self.order[0]
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key
        otherwise, None is returned
        """
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
