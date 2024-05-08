#!/usr/bin/env python3
""" Task 4. Module """
from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    ''' Comment '''
    def __init__(self):
        ''' Initialize derived class with the parent class init method
        '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' Assign to the dictionary self.cache_data the item
        value for the key `key`
        '''
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key
        otherwise, None is returned
        '''
        if key is not None and key in self.cache_data.keys():
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key, None)
        return None
