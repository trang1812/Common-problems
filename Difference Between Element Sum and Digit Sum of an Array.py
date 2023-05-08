# -*- coding: utf-8 -*-
"""
You are given a positive integer array nums.

The element sum is the sum of all the elements in nums.
The digit sum is the sum of all the digits (not necessarily distinct) that appear in nums.
Return the absolute difference between the element sum and digit sum of nums.

Note that the absolute difference between two integers x and y is defined as |x - y|.
"""
class Solution(object):
    def differenceOfSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        element_sum=sum(nums)
        digit_sum=sum(int(digit) for number in nums for digit in str(number))
        difference = abs(element_sum - digit_sum)      
        return difference
