# --------------------------------------
#! /usr/bin/python
# File: 27. Remove Element.py
# Author: Kimberly Gao

# My solution: (Run time: 36ms) (from online website)
# Memory Usage: 14.1 MB
class Solution:
    def _init_(self,name):
        self.name = name

    def removeElement1(self, nums, val) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i

# Another solution: (Run time: 44ms)
    def removeElement2(self, nums, val):
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        return start-1

# Can also use nums.remove() to delete the element (Not suitable for other languages)

if __name__ == '__main__':
    nums = [3,2,2,2,3]
    val = 3
    my_solution = Solution().removeElement1(nums, val)
    print(my_solution)
    another_solution = Solution().removeElement2(nums, val)
    print(another_solution)
