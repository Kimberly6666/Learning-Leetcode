# --------------------------------------
#! /usr/bin/python
# File: 283. Move Zeros.py
# Author: Kimberly Gao

class Solution:
    def _init_(self,name):
        self.name = name

    # My 1st solution: (Run time: 68ms(29.57%)) (2 pointer)
    # Memory Usage: 15.4 MB (61.79%)
    def moveZeros1(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
        for fast in range (slow, len(nums)):
            nums[fast] = 0
        return nums

    # My 2nt solution: (Run time: 72ms(28.1%)) (2 pointer)
    # Memory Usage: 15.5 MB (19.46%)
    def moveZeros2(self, nums):
        slow = 0
        for fast in range(len(nums)):
            i = nums[slow]
            nums[slow] = nums[fast]
            nums[fast] = i
            slow += 1
        return nums

    '''For python, can use
    if num == o:
        nums.remove(num)
        nums.append(num)
    
    Also consider using:
    for slow in xrange(len(nums))
    '''

if __name__ == '__main__':
    nums = [0,1,0,3,12]
    # nums = 0 should be taken into consideration
    my_solution = Solution().moveZeros1(nums)
    print(my_solution)
    better_solution = Solution().moveZeros2(nums)
    print(better_solution)
