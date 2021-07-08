# --------------------------------------
#! /usr/bin/python
# File: ToBegin.py
# Author: Kimberly Gao
# Noted: YOU MUST COMMENT ONE OF THE FUNCTION!

# My solution: (Run time: 40ms)
class Solution:
    def _init_(self,name):
        self.name = name

    def twoSum1(self, nums, target):   # -> List[int]:
        for i, value in enumerate(nums):
            for j in range(i + 1, len(nums)):
                if value + nums[j] == target:
                    list = [i, j]
                    return list
        else:
            print("no match")

# Best solution: (Run time: 24ms)
# Key: Saving every element and the difference value btw it and the target in the dict, the "value" of both them is the
#       indicator in the sums.
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myDict = {}
        for k in range(len(nums)):
            if(nums[k] not in myDict):
                myDict[nums[k]] = k
            value = target - nums[k]
            if(myDict.get(value) !=None and nums[k] >= 0 and myDict[value] != k ):
                return [myDict[value], k]
            myDict[value] = k

if __name__ == '__main__':
    nums = [2,4,5,7,8]
    target = 10
    list1 = Solution().twoSum1(nums, target)
    print(list1)
    list2 = Solution().twoSum2(nums, target)
    print(list2)