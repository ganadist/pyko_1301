import time

def sleep1(duration):
    time.sleep(duration)

class Sleep:
    def __init__(self, duration):
        self.duration = duration

    def sleep(self):
        time.sleep(self.duration)

if __name__ == '__main__':
    import sys

    sleep1(1)
    time.sleep(1)

    s = Sleep(1)
    s.sleep()
