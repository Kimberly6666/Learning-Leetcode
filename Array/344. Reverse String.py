#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 344. Reverse String.py
Description: 
Author: Kimberly Gao
Date: 2021/07/13 11:21 AM
Version: 0.1
Runtime: 412 ms (5.16%)
Memory Usage: 18.5 MB (64.61%)
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Two pointers: head & tail
        :type s: List[str]
        :rtype: None
        """
        head, tail = 0, len(s)-1
        while head < tail:
            crt = s[head]
            s[head] = s[tail]
            s[tail] = crt
            head += 1
            tail -= 1
