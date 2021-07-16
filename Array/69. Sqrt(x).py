#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 69. Sqrt(x).py
Author: Kimberly Gao
Date: 2021/07/16 4:19 PM
Version: 0.1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
