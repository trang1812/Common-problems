# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 15:47:39 2023

@author: Win 10
"""

'''Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string '''.

#Solution1
class Solution(object):
    def longestCommonPrefix(self,strs):
        prefix= min(strs, key=len)
        strs.remove(prefix)
        for s in strs:
            for i in range(len(prefix)):
                if prefix[i] != s[i]:
                    prefix=s[:i]
                    break
            if len(prefix) == 0:
                print("")
        return prefix
    
#Solution2
class Solution(object):
    def longestCommonPrefix(self, strs):
        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix
    
strs = ["ab","a", "abc"]
Solution().longestCommonPrefix(strs)