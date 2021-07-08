# --------------------------------------
#! /usr/bin/python
# File: ToBegin.py
# Author: Kimberly Gao

# My solution: (Run time: 28ms)
# Memory Usage: 14.4 MB
class Solution:
    def _init_(self,name):
        self.name = name

    def reverse1(self, x: int) -> int:
        string = str(x)
        list1 = list(string)
        if list1[0] == '-':
            list_no_sign = list1[1:] # remove the sign
            list_reverse = list_no_sign[::-1] # reverse the numbers
            list_reverse.insert(0, '-')
        else:
            list_reverse = list1[::-1]
        num_reverse_str = ''.join(list_reverse) # ['3','2','1'] -> ['321']
        num_reverse = int(num_reverse_str)
        if num_reverse < pow(2, 31)-1 and num_reverse >= -pow(2, 31):
            return num_reverse
        else:
            return 0

# Best solution: (Run time: 20ms)
    def reverse2(self, x: int):
        rev, flg = 0, 1
        if x < 0:
            flg = -1
            x = abs(x)
        while (x):
            unit = x % 10
            rev = rev * 10 + unit
            x = x // 10
        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        return rev * flg

if __name__ == '__main__':
    x = 1534236469
    # x = 15346
    my_solution = Solution().reverse1(x)
    print(my_solution)
    best_solution = Solution().reverse2(x)
    print(best_solution)