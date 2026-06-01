#!/usr/bin/python3
"""
Module that creates a pascal_triangle function
"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n

    Args:
        n (int): The number of rows of Pascal's triangle
    Returns:
        list: List of lists representing Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
