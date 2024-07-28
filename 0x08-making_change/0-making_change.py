#!/usr/bin/python3
"""Solution of makechange problem """


def makeChange(coins, total):
    """returns the minimum coins to make change"""
    coins.sort()
    count = 0
    for coin in range(len(coins)-1, -1):
        while total - coin >= 0:
            count += 1
            total -= total - coin
    if coin:
        return -1
    return count
