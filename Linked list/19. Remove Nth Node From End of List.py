#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 19. Remove Nth Node From End of List.py
Description: 
Author: Kimberly Gao
Date: 2021/07/16 5:08 PM
Version: 0.1
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # dummy_head = ListNode()
        # dummy_head.next = head
        
        dummy_head = ListNode(next = head)
        fast, slow = dummy_head, dummy_head
        
        while(n != 0):
            fast = fast.next
            n -=1            
        while(fast.next != None):
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy_head.next
