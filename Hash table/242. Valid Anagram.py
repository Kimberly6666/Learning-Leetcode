#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 242. Valid Anagram.py
Author: Kimberly Gao
Date: 2021/07/22 2:10 PM
Version: 0.1
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in range(len(s)):
            record[ord(s[i])-ord("a")] += 1
        
        for i in range(len(t)):
            record[ord(t[i])-ord("a")] -= 1
            
        for i in range(len(record)):
            if record[i] != 0:
                return False
        return True
