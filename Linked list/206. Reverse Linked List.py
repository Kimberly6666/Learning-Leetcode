
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 206. Reverse Linked List.py
Author: Kimberly Gao
Date: 2021/07/15 11:19 PM
Version: 0.1
"""
# Approach 1: Iteration (two pointers)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        while(cur != None):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
      
# Approach 2: Recursion (two pointers)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        def reverse(pre,cur):
            if not cur:
                return pre
                
            tmp = cur.next
            cur.next = pre

            return reverse(cur,tmp)
        
        return reverse(None,head)
