# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Basically the pattern we are trying to get here is
we have a list

0 1 2

On the first iteration we want there to be a link which looks like
0 <- 1 2

And on the second iteration we want there to be a link which looks something
like

0 <- 1 <- 2

The tricky bit is realizing that we have to store the next val before incrementing
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_val = curr.next
            curr.next = prev
            prev = curr
            curr = next_val
        
        return prev