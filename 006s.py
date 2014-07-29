#!/usr/bin/env python

import time

start = time.time()

x = sum(range(1,101))**2
y = sum(y**2 for y in range(1,101))
n = x - y

print n

elapsed = (time.time()-start)

print "time: %s seconds" % elapsed
