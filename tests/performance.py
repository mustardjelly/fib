"""Testing setup for performance metrics"""

import logging
import random
import time
from typing import Callable
from src.fibonacci import fibonacci, fib_no_cache

# Constants
SEED = 42
FIBS_TO_MAKE = 11
RAND_RANGE = (0, 40)


def configuration():
    """Runs performance configurations"""
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s: %(message)s",
    )
    random.seed(SEED)


def time_it(func: Callable[[int], int]) -> float:
    """Times the passed in fib fuinction."""
    logging.info("Running %s", func.__name__)
    start: float = time.time()
    for i in range(FIBS_TO_MAKE):
        value: int = random.randint(*RAND_RANGE)
        res: int = func(value)
        # pylint: disable=logging-fstring-interpolation
        logging.debug(f"{i:2} - f({value:2}) = {res:14}")
    finish: float = time.time()
    elapsed: float = finish - start
    return elapsed


def call_one() -> float:
    """Non-caching call"""
    return time_it(fib_no_cache)


def call_two() -> float:
    """First caching call"""
    fibonacci.cache_clear()
    return time_it(fibonacci)


def call_three() -> float:
    """Second caching call"""
    return time_it(fibonacci)


def main() -> None:
    """Call the things"""

    print("Cached time: ", call_one())
    print("No cache time (1): ", call_two())
    print(fibonacci.cache_info())
    print("No cache time (2): ", call_three())
    print(fibonacci.cache_info())


if __name__ == "__main__":
    main()
