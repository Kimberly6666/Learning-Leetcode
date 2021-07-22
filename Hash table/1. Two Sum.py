#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 1. Two Sum.py
Author: Kimberly Gao
Date: 2021/07/16 5:21 PM
Version: 0.1
"""

# 使用数组和set来做哈希法的局限:
# 1. 数组的大小是受限制的，而且如果元素很少，而哈希值太大会造成内存空间的浪费。
# 2. set是一个集合，里面放的元素只能是一个key，而两数之和这道题目，不仅要判断y是否存在而且还要记录y的下表位置，因为要返回x 和 y的下表。所以set 也不能用。

# map是一种key value的存储结构，可以用key保存数值，用value在保存数值所在的下表。

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num] = ind
        for i,num in enumerate(nums):
            j = hashmap.get(target - num)
            if j is not None and i!=j:
                return [i,j]
              
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,value in enumerate(nums):
            for j in range(i+1,len(nums)):
                if value + nums[j] == target:
                    list = [i,j]
                    return list
        else:
            print("no match")
