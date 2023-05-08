# -*- coding: utf-8 -*-
"""
Given a signed 32-bit integer x, return x with its digits reversed. 
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], 
then return 0.
"""

class Solution(object):
    def reverse(self, x):
            str_x = str(abs(x))
        if x < 0:
            reversed_x=int(str_x[::-1])*(-1)
        else: 
            reversed_x=int(str_x[::-1])
        return reversed_x if reversed_x >= -(2**31) and reversed_x <= (2**31 - 1) else 0

x=-1205450
Solution().reverse(x)
