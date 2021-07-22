#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 202. Happy Number.py 
Author: Kimberly Gao
Date: 2021/07/22 3:28 PM
Version: 0.1
"""

# When we encounter the need to quickly determine whether an element appears in the set, we'd better consider hashing
class Solution:
    def isHappy(self, n: int) -> bool:
        result_set = set()
        while (n > 0):
            sqrSum = self.getSum(n)
            if sqrSum == 1:
                return True
            if sqrSum in result_set:
                return False
            else:
                result_set.add(sqrSum)
                n = sqrSum
       
        
    def getSum(self, n:int) -> int:
        sqrSum = 0
        while(n > 0):
            sqrSum = sqrSum + (n % 10) * (n % 10)
            n //= 10
        return sqrSum
