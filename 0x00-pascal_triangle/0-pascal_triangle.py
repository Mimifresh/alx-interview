#!/usr/bin/python3
""" returns a list of lists of integers representing the Pascal’s triangle of n"""

def pascal_triangle(n):
    """checks if row is empty"""
    lst = []
    if n <= 0:
        return []
    for i in range(n):
        child = [1]
        for j in range(i):
            res = 0
            j = j + 1
            res = lst[i - 1][j - 1]
            if j < i:
                res += lst[i - 1][j]
            child.append(res)
        lst.append(child)

    return lst
