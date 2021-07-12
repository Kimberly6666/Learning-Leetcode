# --------------------------------------
#! /usr/bin/python
# File: 977. Squared of a Sorted Array.py
# Author: Kimberly Gao

# My solution: (Run time: 132ms) (from website)
# Memory Usage: 15.6 MB
class Solution:
    def _init_(self,name):
        self.name = name

    # Only for python. Using function sort()
    # Will overwritting the inputs
    def sortedSquares1(self, nums):
        for i in range(nums):
            nums[i] *= nums[i]
        nums.sort()
        return nums

    # Making a new array, not in place, O(n) auxiliary space
    def sortedSquares2(self, nums):
        return sorted([v**2 for v in nums])

    # Making a new array, not in place, O(1) auxiliary space
    def sortedSquares3(self, nums):
        newlist = [v**2 for v in nums]
        newlist.sort()  # This is in place!
        return newlist

    # Two pointers:
    def sortedSquares4(self, nums):
        # list comprehension: return a list with all None elements (its length=length of nums):
        # result = [None for _ in nums]
        result = [None] * len(nums)  # 10x faster than above one
        left, right = 0, len(nums) - 1
        for index in range(len(nums)-1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] ** 2
                left += 1
            else:
                result[index] = nums[right] ** 2
                right -= 1
        return result

if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    solution = Solution().sortedSquares4(nums)
    print(solution)