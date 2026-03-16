from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        print(f"Calling: {func.__name__}")
        result = func(args, kargs)
        print(f"Finished: {func.__name__}")
        return result
    return wrapper

@logger
def make_chai(type, sugar):
    print(f"Making chai {type} {sugar}")

make_chai("Masala", sugar = "low")