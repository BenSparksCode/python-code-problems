from typing import Callable
import time

def timer(func: Callable) -> Callable:
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()

        print()
        print("-------------------------------------------------------------")
        print(f"|\tFunction {func.__name__}() executed in:")
        print("|")
        print(f"|\t\t\t{end_time - start_time:.8f} seconds")
        print("-------------------------------------------------------------")
        print()

        return result
    return wrapper