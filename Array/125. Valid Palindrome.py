# --------------------------------------
#! /usr/bin/python
# File: ToBegin.py
# Author: Kimberly Gao
import string

class Solution:
    def _init_(self,name):
        self.name = name

    # My solution: (Run time: 80ms)
    # Memory Usage: 14.6 MB
    def isPalindrome1(self, s: str) -> bool:
        s_new = ""
        n = 0
        a = ord("a")
        z = ord("z")
        a_cpt = ord("A")
        z_cpt = ord("Z")
        zero = ord("0")
        nine = ord("9")

        for i in range(len(s)):
            if (a <= ord(s[i]) and ord(s[i]) <= z) or (a_cpt <= ord(s[i]) and ord(s[i]) <= z_cpt) or (zero <= ord(s[i]) and ord(s[i]) <= nine):
                s_new = s_new + s[i]

        if len(s_new) % 2 == 0:
            # even
            for k in range(len(s_new) // 2):
                if ord(s_new[k]) - ord(s_new[-(k+1)]) == 0 \
                        or ((a <= ord(s_new[k]) and ord(s_new[k]) <= z) and (abs(ord(s_new[k]) - ord(s_new[-(k+1)])) == 32))\
                        or ((a <= ord(s_new[-(k+1)]) and ord(s_new[-(k+1)]) <= z) and (abs(ord(s_new[k]) - ord(s_new[-(k+1)])) == 32)):
                    n = n + 1
            if n == len(s_new)//2:
                return True
            else:
                return False

        else:
            # odd
            for k in range((len(s_new) + 1) // 2):
                if ord(s_new[k]) - ord(s_new[-(k + 1)]) == 0 \
                        or ((a <= ord(s_new[k]) and ord(s_new[k]) <= z) and (abs(ord(s_new[k]) - ord(s_new[-(k + 1)])) == 32)) \
                        or ((a <= ord(s_new[-(k + 1)]) and ord(s_new[-(k + 1)]) <= z) and (abs(ord(s_new[k]) - ord(s_new[-(k + 1)])) == 32)):
                    n = n + 1
            if n == (len(s_new) + 1) // 2:
                return True
            else:
                return False


# Best solution: (Run time: 20ms)
    def isPalindrome2(self, s: str) -> bool:
        for i in string.punctuation:
            s = s.replace(i, "")  # remove any signs
        s = s.replace(" ", '').lower() # remove space

        return s == s[::-1]

if __name__ == '__main__':
    # s = "A man, a plan, a canal: Panama" # Capital/little letter
    # s = "A" # if there's only one letter
    # s = "Never a foot too far, even."
    s = "0P"  # Special case! Cannot use "+32" easily

    my_solution = Solution().isPalindrome1(s)
    print(my_solution)
    best_solution = Solution().isPalindrome2(s)
    print(best_solution)