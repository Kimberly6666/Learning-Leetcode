# --------------------------------------
#! /usr/bin/python
# File: 26. Remove Duplicates from Sorted Array.py
# Author: Kimberly Gao

# My solution: (Run time: 132ms) (2 pointer)
# Memory Usage: 15.6 MB
class Solution:
    def _init_(self,name):
        self.name = name

    def removeDuplicates1(self, nums) -> int:
        # I forgot to consider the occasion that list is empty
        if len(nums) == 0: return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

    # Better solution: (100% less memory, 96% faster)
    # Take advantage of "sorted"
    def removeDuplicates2(self, nums):
        length = 0
        if len(nums) == 0: return 0
        for i in range(1,len(nums)):
            if nums[length] < nums[i]:
                length += 1
                nums[length] = nums[i]
        return length + 1

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    my_solution = Solution().removeDuplicates1(nums)
    print(my_solution)
    better_solution = Solution().removeDuplicates2(nums)
    print(better_solution)