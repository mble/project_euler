#!/usr/bin/env python

import itertools
import time

start = time.time()

# Sieve of Eratosthenes from:
# http://rosettacode.org/wiki/Sieve_of_Eratosthenes#Infinite_generator_with_a_faster_algorithm
# An odds only incremental Sieve of Eratosthenes
def eratosthenes():
    """Yields the sequence of prime numbers using the Sieve of Eratosthenes."""
    yield 2; yield 3; yield 5; yield 7;
    bps = (p for p in eratosthenes())       # additional primes supply
    p = next(bps) and next(bps)             # discard 2, then get 3
    q = p * p                               # 9 - square of next prime to be put
    sieve = {}                              #       into sieve dict
    n = 9                                   # the initial candidate number
    while True:
        if n not in sieve:                  # is not a multiple of previously recorded primes
            if n < q:
                yield n                     # n is prime
            else:
                p2 = p + p                  # n == p * p: for prime p, add p * p + 2 * p,
                sieve[q + p2] = p2          #               with 2 * p as incremental step
                p = next(bps); q = p * p    # advance base prime and next prime to be put
        else:
            s = sieve.pop(n); nxt = n + s   # n is composite, advance
            while nxt in sieve: nxt += s    # ensure each entry is unique
            sieve[nxt] = s                  # next non-marked multiple of this prime
        n += 2                              # work on odds only
# End SoE

print sum(itertools.takewhile(lambda x: x < 2e6, eratosthenes()))

elapsed = (time.time() - start)

print "time: %s seconds" % elapsed

