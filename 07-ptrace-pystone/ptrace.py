#!/usr/bin/env python

# python implementation of
# http://people.gnome.org/~federico/news-2006-03.html#login-time-2

import os, sys

__all__ = ["traceLog", "Trace", "trace"]

_USE_TRACE = os.environ.get('ENABLE_PTRACE', '0') == '1'

if _USE_TRACE:
    _MARK = ': '.join(('MARK', sys.argv[0], ''))
    def traceLog(name):
        os.access(_MARK + name, os.F_OK)

    class Trace:
        def __init__(self, name):
            self.name = name
            traceLog(name + "_enter")
        def __del__(self):
            traceLog(self.name + "_exit")

else:
    traceLog = lambda name: None
    Trace = lambda name: None

class trace:
    def __init__(self, name = ''):
        self.name = name

    def __call__(self, func):
        if not _USE_TRACE:
            return func

        if not self.name:
            self.name = func.__name__
        def wrapper(*args, **kwds):
            traceLog(self.name + "_enter")
            r = func(*args, **kwds)
            traceLog(self.name + "_exit")
            return r
        return wrapper

def main():
    import time

    @trace()
    def sleep(duration):
        time.sleep(duration)

    class Sleep:
        @trace('Sleep.__init__')
        def __init__(self):
            pass

        @trace('Sleep.sleep')
        def sleep(self, duration):
            time.sleep(duration)

    # test manual trace
    t = Trace('time.sleep')
    time.sleep(1)
    del t

    time.sleep(1)

    # test trace decorator
    sleep(1)

    s = Sleep()
    s.sleep(1)

if __name__ == '__main__':
    main()

# vim: ts=4 st=4 sts=4 expandtab syntax=python
