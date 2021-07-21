# Noted:   
1. On Leetcode, 'head' is the first node if linked list.    
2. On the other textbooks, 'head' is a virtual point, which saves the address on the first node.    
3. As for pointers, like 'cur = head', cur is a node which has the same val as head, and their 'next' pointers are the same. 
4. So here, cur is not an actual pointer like 'next' pointer.    

# Conclusion:
1. Adding dummy head: deleting duplicated nodes, reversing the linked list.
2. Two pointers: if there's a circle/where's the circle entry, if there's an intersection,deleting the middle node, deleting the nth node
3. If inversion is involved, consider using the stack first.
