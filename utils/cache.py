import functools
from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=300)  # 5 minute TTL

def cache_result(ttl: int = 300):
    """Cache the result of a function"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = f"{func.__module__}:{func.__name__}:{args}:{kwargs}"
            result = cache.get(key)
            if result is None:
                result = func(*args, **kwargs)
                cache[key] = result
            return result
        return wrapper
    return decorator
