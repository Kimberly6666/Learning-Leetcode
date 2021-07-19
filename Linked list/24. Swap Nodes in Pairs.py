
#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
FileName: 24. Swap Nodes in Pairs.py
Description: 
Author: Kimberly Gao
Date: 2021/07/19 6:27 PM
Version: 0.1
"""
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0) 
        dummy.next = head
        cur = dummy
        while cur.next and cur.next.next: 
            tmp = cur.next 
            tmp1 = cur.next.next.next 
            
            cur.next = cur.next.next          # Step 1
            cur.next.next = tmp               # Step 2
            cur.next.next.next = tmp1         # Step 3
            
            cur = cur.next.next 
        # Moving cur.next is equal to moving dummy_head.next
        return dummy.next
