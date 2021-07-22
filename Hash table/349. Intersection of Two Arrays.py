#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 349. Intersection of Two Arrays.py
Author: Kimberly Gao
Date: 2021/07/16 5:21 PM
Version: 0.1
"""

# set is unordered
# set cannot contain duplicated elements 
# the elements cannot be inquiried by index

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result_set = set()
        set1 = set(num1)
        for ele in num2:
            if ele in set1:
                result_set.add(ele)
        return result_set
