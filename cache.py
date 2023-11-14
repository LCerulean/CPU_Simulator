#needs a store limit
#method for removing old/unneeded data from the cache
    #way to choose/prioritize commonly used data over data that is not often in use

import collections

max_size = 16

class Cache:
    # Inside cache list "address" and "value" are stored as tuples (address, value)
    def __init__(self):
        self.cache = collections.deque(maxlen=max_size)
        self.clear_cache()

    # Appends entire cashe, overwriting the list of tuples
    def clear_cache(self):
        for i in range(max_size):
            self.cache.append(("", ""))

    # Returns tuple if found in cache
    def search_cache(self, address):
        for i in range(max_size):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None

    # Adds address and value to cache as a tuple (address, value)
    def write_cache(self, address, value):
        self.cache.append(tuple((address, value)))