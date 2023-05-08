# -*- coding: utf-8 -*-

"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        left=0
        d=set()
        count=0
        for right in range(len(s)):
            while s[right] in d:
                d.remove(s[left])
                left+=1
            d.add(s[right])
            count=max(count,right-left+1)
        return count
        
    

s="abcabb"
Solution().lengthOfLongestSubstring(s)
