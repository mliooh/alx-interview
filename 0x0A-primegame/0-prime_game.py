#!/usr/bin/python3
""" Prime Game """


def isWinner(x, nums):
    """ Prime Game """
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = False
    sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    c = 0
    for i in range(len(sieve)):
        if sieve[i]:
            c += 1
        sieve[i] = c
    p1 = 0
    for n in nums:
        p1 += sieve[n] % 2 == 1
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 > len(nums):
        return "Maria"
    return "Ben"