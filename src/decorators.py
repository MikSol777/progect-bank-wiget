from functools import wraps


def log(filename=None):
    """Логирует выполнения функции, а также ее результаты или возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} ok")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception:
                if filename:
                    with open(filename, "w", encoding="utf-8") as file:
                        file.write(f"{func.__name__} error: TypeError Inputs: {args}, {kwargs}")
                else:
                    print(f"{func.__name__} error: TypeError Inputs: {args}, {kwargs}")

        return inner

    return decorator
