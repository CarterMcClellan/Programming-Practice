# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        if list1 and list2:
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        elif list1:
            head = list1
            list1 = list1.next
        elif list2:
            head = list2
            list2 = list2.next
        else:
            return None

        curr = head
        while list1 and list2:
            if list1.val == list2.val:
                next1, next2 = list1.next, list2.next
                curr.next = list1
                curr = curr.next
                curr.next = list2
                list1, list2 = next1, next2
            
            elif list1.val < list2.val:
                next1 = list1.next
                curr.next = list1
                list1 = next1
            
            else:
                next2 = list2.next
                curr.next = list2
                list2 = next2
            curr = curr.next
            
        remaining_list = None
        if list1:
            remaining_list = list1
        else:
            remaining_list = list2

        curr.next = remaining_list
            
        return head