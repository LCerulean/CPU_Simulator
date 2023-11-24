#Cache temporarily stores date and located directly on the processor

from collections import deque

cache_size = 8

class Cache:
    # Inside cache list "address" and "data" are stored as tuples (address, data)
    def __init__(self):
        #deque used to automatically re-write the cache (first in, first out) when it is full
        self.cache = deque(maxlen=cache_size)
        self.flush_cache()
        self.cache_on = True

    # Appends entire cashe, removing all tuples by appending blank values until max is reached
    def flush_cache(self):
        for i in range(cache_size):
            self.cache.append(("", ""))

    # Returns value if address is found in cache
    def search_cache(self, address):
        for i in range(cache_size):
            if self.cache[i][0] == address:
                return self.cache[i][1]
        return None

    # Adds address and data to cache as a tuple (address, data)
    def write_cache(self, address, data):
        self.cache.append(tuple((address, data)))