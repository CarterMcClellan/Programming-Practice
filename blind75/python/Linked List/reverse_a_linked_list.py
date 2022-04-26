# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        # if list is length 1
        if not head or not head.next:
            return head
        
        while head.next:
            stack.append(head)
            head = head.next
        
        last = head
        while stack:
            curr = stack.pop(-1)
            last.next = curr
            last = curr
        last.next = None
        
        return head
