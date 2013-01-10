#!/usr/bin/env python
#Problem 9:
    #A Pythagorean Triplet (PT) is a triplet of numbers (a,b,c) in N
    #such that a**2 + b**2 == c**2. There is one PT which sums to 1000.
    #Find its product.

from itertools import combinations

def pythagorean_triplet(m, n):
    '''
    Return the PT generated from the positive integers m & n, where m > n.
    Algorithm: Euclid's forumla:
        http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple

    :Parameters:
        -   `m`: a :class:`int` greater than 0.
        -   `n`: a :class:`int` greater than 0, less than `m`.
    '''
    return (abs(m**2 - n**2), 2*m*n, m**2 + n**2)

def generate_candidate_pairs(m, n):
    return [pythagorean_triplet(*pair) for pair in combinations(xrange(m,n), 2)]

def main():
    #triple(20, 21) = (41, 840, 841); 41+840+841 >> 1000
    #therefore, the answer will be generated by some (m,n) < (19, 20)
    candidate_pairs = generate_candidate_pairs(1, 21)
    candidate_pair_sums = [sum(i) for i in candidate_pairs]
    winner = [i for n,i in enumerate(candidate_pairs) if candidate_pair_sums[n] == 1000][0]
    print winner[0]*winner[1]*winner[2] 

if __name__ == '__main__':
    main()
