from typing import Callable, Any


def cache(func: Callable) -> Callable:
    cash_dict = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        tuple_kwargs = tuple(sorted(kwargs.items()))
        tuple_a_and_k = (args, tuple_kwargs)
        if tuple_a_and_k in cash_dict:
            print("Getting from cache")
            return cash_dict[tuple_a_and_k]
        else:
            print("Calculating new result")
            result = cash_dict[tuple_a_and_k] = func(*args, **kwargs)
            return result
    return wrapper
