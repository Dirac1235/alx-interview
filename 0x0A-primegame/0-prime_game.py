#!/usr/bin/python3
"""Solution file for Prime Game"""


def isWinner(x, nums):
    """returns the winner for the prime game"""
    players = [0, 0]
    turn = 0
    for j in range(x):
        rounds = [0, 0]
        primecontainer = [[k, True] for k in range(nums[j] + 1)]
        for i in range(2, len(primecontainer)):
            if primecontainer[i][1]:
                if turn == 0:
                    rounds[0] += 1
                    turn = 1
                else:
                    rounds[1] += 1
                    turn = 0
                    add = i
                while i + add < len(primecontainer):
                    primecontainer[i + add][1] = False
                    i += add
        if rounds[0] > rounds[1]:
            players[0] += 1
        else:
            players[1] += 1
    if players[0] > players[1]:
        return "Maria"
    else:
        return "Ben"
