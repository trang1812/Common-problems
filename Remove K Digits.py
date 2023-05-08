# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:06:54 2023

@author: Win 10
"""

"""
Given string num representing a non-negative integer num, and an integer k, 
return the smallest possible integer after removing k digits from num.
"""

def removeKdigits(num, k):
    stack = []
    for digit in num:
        while k > 0 and stack and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    while k > 0:
        stack.pop()
        k -= 1
    result = ''.join(stack).lstrip('0')
    print(stack)
    return result if result else '0'

num='8231923'
k=2
removeKdigits(num, k)


