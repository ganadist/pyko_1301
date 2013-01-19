import time

def sleep(duration):
    start = time.time()
    time.sleep(duration)
    end = time.time()
    print 'sleep()', start, end - start

if __name__ == '__main__':
    sleep(1)

