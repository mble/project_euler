#!/usr/bin/env python

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = 1
for i in xrange(1,21):
    n = lcm(n, i)
print n
