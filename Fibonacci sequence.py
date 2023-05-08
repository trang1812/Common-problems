# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:46:55 2023

@author: Win 10
"""

'''The sequence 0, 1, 1, 2, 3, 5, 8, 13, 21,... is called the Fibonacci sequence. The first two numbers are 0 and 1 and each following number is the sum of the two preceding ones.
Write a Python function to generate and print the elements of the sequence less than or equal to the value passed to the function
'''

# n elements in the sequence
def fib_first(n):
    previous = 0
    current = 1
    for _ in range(n):
        print(previous, end=' ')
        previous, current = current, previous + current
    print()

fib_first(11)

# element <=n
def fib_lte(n):
    previous = 0
    current = 1
    while previous <= n:
        print(previous, end=' ')
        previous, current = current, previous + current
    print()
fib_lte(111)