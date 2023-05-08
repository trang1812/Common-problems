# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:49:43 2023

@author: Win 10
"""

#Given a roman numeral, convert it to an integer

class Solution(object):
    def romanToInt(self, s):
        roman = {
           'I': 1,
           'V': 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000
        }
        integer = 0

        for x, y in zip(s, s[1:]):
            if roman[x] < roman[y]:
                integer -= roman[x]
            else:
                integer += roman[x]

        return integer + roman[s[-1]]
    
#test
x=Solution()
print(x.romanToInt("XVIII"))