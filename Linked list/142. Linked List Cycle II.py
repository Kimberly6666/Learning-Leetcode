#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 142. Linked List Cycle II.py
Author: Kimberly Gao
Date: 2021/07/20 6:31 PM
Version: 0.1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return None
        slow, fast = head, head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                temp = head
                while(temp != fast):
                    fast = fast.next
                    temp = temp.next
                return temp
        return None
