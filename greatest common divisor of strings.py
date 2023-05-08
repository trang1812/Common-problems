# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 10:52:48 2023

@author: Win 10
"""
"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


def gcd(a, b):
    """Returns the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def largest_common_divisor(str1, str2):
    n, m = len(str1), len(str2)
    d = gcd(n, m)
    substring = str1[:d]
    if substring * (n // d) == str1 and substring * (m // d) == str2:
        return substring
    return ""
str2 = "ABCABC"
str1 = "ABC"
largest_common_divisor(str1, str2)

