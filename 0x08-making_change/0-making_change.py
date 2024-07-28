#!/usr/bin/python3
"""Solution of makechange problem """


def makeChange(coins, total):
    """returns the minimum coins to make change"""
    coins.sort()
    count = 0
    for coin in range(len(coins)-1, -1, -1):
        while total - coins[coin] >= 0:
            count += 1
            total -= coins[coin]
    if total:
        return -1
    return count
