#!/usr/bin/env python

import time

start = time.time()

def pythagtrips():
    for a in range(1, 500 + 1):
        for b in range(1, 500 + 1):
            c = 1000 - b - a
            if c * c == a * a + b * b:
                return a * b * c

print pythagtrips()

elapsed = (time.time() - start)

print "time: %s seconds" % elapsed
