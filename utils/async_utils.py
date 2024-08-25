import asyncio

async def async_wait_for(func, timeout: int = 10):
    """Wait for an async function to complete"""
    try:
        return await asyncio.wait_for(func(), timeout=timeout)
    except asyncio.TimeoutError:
        raise TimeoutError(f"Timeout waiting for {func.__name__}")

async def async_retry(func, max_retries: int = 3, delay: int = 1):
    """Retry an async function on failure"""
    for i in range(max_retries):
        try:
            return await func()
        except Exception as e:
            if i < max_retries - 1:
                await asyncio.sleep(delay)
            else:
                raise e
