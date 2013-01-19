import time
from ptrace import trace

@trace()
def sleep1(duration):
    time.sleep(duration)

class Sleep:
    @trace('Sleep.__init__')
    def __init__(self, duration):
        self.duration = duration

    @trace('Sleep.sleep')
    def sleep(self):
        time.sleep(self.duration)

if __name__ == '__main__':
    import sys

    sleep1(1)
    time.sleep(1)

    s = Sleep(1)
    s.sleep()
