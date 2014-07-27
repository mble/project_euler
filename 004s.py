#!/usr/bin/env python

n = 0
for a in xrange(100, 1000):
     for b in xrange(a, 1000):
         x = a * b
         if x > n:
             s = str(x)
             if s == s[::-1]:
                 n = a * b

print n
