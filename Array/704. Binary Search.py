#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 704. Binary Search.py
Description: 
Author: Kimberly Gao
Date: 2021/07/15 11:19 PM
Version: 0.1
"""

# Approach 1:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return -1
      
# Approach 2:
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right  =0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1
      
  # Approach 3: (Only for Python)
  class Solution:
    def search(self, nums, target):
        index = bisect.bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1
      
      
