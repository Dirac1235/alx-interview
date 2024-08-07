#!/usr/bin/python3
"""Solution file for island perimeter"""


def island_perimeter(grid):
    """Returns the island perimeter"""
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if i - 1 < 0:
                    perimeter += 1
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    perimeter += 1
                if i + 1 < len(grid) and grid[i + 1][j] == 0:
                    perimeter += 1
                if i + 1 >= len(grid):
                    perimeter += 1
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    perimeter += 1
                if j - 1 < 0:
                    perimeter += 1
                if j + 1 < len(grid[i]) and grid[i][j + 1] == 0:
                    perimeter += 1
                if j + 1 >= len(grid[i]):
                    perimeter += 1
    return perimeter
