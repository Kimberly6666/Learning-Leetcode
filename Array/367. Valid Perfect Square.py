#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 367. Valid Perfect Square.py
Description: 
Author: Kimberly Gao
Date: 2021/07/16 5:21 PM
Version: 0.1
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
            else:
                return True
        return False
