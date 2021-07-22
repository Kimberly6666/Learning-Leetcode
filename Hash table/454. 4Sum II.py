#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 454. 4Sum II.py
Author: Kimberly Gao
Date: 2021/07/22 4:57 PM
Version: 0.1
"""

# It's different with the qns of "the sum of n numbers".
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashmap = {}  # hashmap = dict()
        count = 0
        for i in nums1:
            for j in nums2:
                if i + j in hashmap:
                    hashmap[i + j] += 1
                else:
                    hashmap[i + j] = 1
        
        for i in nums3:
            for j in nums4:
                if (0 - i - j) in hashmap:
                    count += hashmap[0 - i - j]
        return count
