import time

def trace(func):
    def wrapper(*args, **kwds):
        start = time.time()
        r = func(*args, **kwds)
        end = time.time()
        print func.__name__ + '()', start, end - start
        return r
    return wrapper
        
@trace
def sleep(duration):
    time.sleep(duration)

if __name__ == '__main__':
    sleep(1)

