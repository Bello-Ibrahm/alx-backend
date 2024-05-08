#!/usr/bin/env python3
""" Task 0. Module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' Comment '''
    def __init__(self):
        ''' Initialize derived class with the parent class init method
        '''
        BaseCaching.__init__(self)

    def put(self, key, item):
        ''' Assign to the dictionary self.cache_data the item
        value for the key `key`
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' Returns the value in self.cache_data linked to key
        otherwise, None is returned
        '''
        if key is not None and key in self.cache_data.keys():
            return self.cache_data[key]
        return None
