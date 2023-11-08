from typing import Callable
import time

def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print()
        print("----------------  RUN TIME  ---------------")
        print("-\t%s seconds\t  -" % (end_time - start_time))
        print("-------------------------------------------")
        print()
        return result
    return wrapper