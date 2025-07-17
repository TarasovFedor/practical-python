import time

def timethis(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            end = time.time()
            print(f'{func.__module__}.{func.__name__}: {end-start}')
    return wrapper


if __name__ == '__main__':
    @timethis
    def countdown(n, end = 0):
        while n > end:
            n -= 1

    countdown(100000)