# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head.next, head
        while slow:
            if fast and slow.val == fast.val:
                return True

            if fast and fast.next:
                fast = fast.next.next
            else:
                fast = None

            slow = slow.next

        return False