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
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left < right:

            middle = (left + right) // 2
            
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else: 
                return middle
            
        return left if target <= nums[left] else left+1
 
# Approach 2: (Modification is needed!!!)
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)
        while left + 1 < right:

            middle = (left + right) // 2
            
            if nums[middle] > target:
                right = middle
            elif nums[middle] < target:
                left = middle + 1
            else: 
                return middle
            
        return left if target <= nums[left] else left+1
      
# Approach 3: (Other's solution. Only for Python.)
class Solution:
    def searchInsert(self, N: List[int], t: int) -> int:
        return bisect.bisect_left(N,t)
      
# Approach 4: Linear scan (Other's solution. Only for Python.)
class Solution:
    def searchInsert(self, N: List[int], t: int) -> int:
    	for i,n in enumerate(N):
    		if n >= t: return i
    	return len(N)
    
# Approach 5: Linear scan (Other's solution. Only for Python.)
# Need to import math module
class Solution:
    def searchInsert(self, N: List[int], t: int) -> int:
    	for i,n in enumerate(N+[math.inf]):
    		if n >= t: return i
