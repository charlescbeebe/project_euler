#!/usr/bin/env python
#Problem 10:
    #The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    #Find the sum of all the primes below two million.

from itertools import combinations_with_replacement
from math import ceil

def sieve_of_sundaram(n):
    '''
    Return a list of primes below (2`n`+2).
    :Parameters:
        - `n`: a :class:`int` determines the upper limit to numbers that are
        searched.
    '''
    candidates = {i:1 for i in xrange(1, n+1)}
    max_i_or_j = int(ceil( n/3.0 )) #i+j+2ij <= n & 1 <= i <= j, max(i) = max(j) = n/3
    for i,j in combinations_with_replacement(xrange(1, max_i_or_j), 2):
        k = i + j + (i*j<<1)
        candidates.pop(k, None)
    return [2] + [(i<<1) + 1 for i in sorted(candidates.keys())]

def main():
    primes_lt_2m = sieve_of_sundaram((2000000-2)/2)
    print sum(primes_lt_2m)

if __name__ == '__main__':
    main()
