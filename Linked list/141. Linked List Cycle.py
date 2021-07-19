#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 141. Linked List Cycle.py
Author: Kimberly Gao
Date: 2021/07/15 9:10 PM
Version: 0.1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        slow, fast = head, head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if fast == slow: # two pointers meet
                    return True
        return False
