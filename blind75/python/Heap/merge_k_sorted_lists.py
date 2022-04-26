# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        if all(list is None for list in lists):
            return None
        
        master_list = lists[0]
        for llist in lists[1:]:
            if llist and master_list and llist.val < master_list.val:
                master_list = self.merge_2_lists(llist, master_list)
            else:
                master_list = self.merge_2_lists(master_list, llist)

        return master_list
    
    def merge_2_lists(self, list1, list2):
        """ merge list1 and list2 """
        
        # l1 = [1, 1, 3, 4, 4, 5]
        # l2 = [2, 6]
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head = list1
        while list1.next and list2.next:
            # l2 value can be inserted in between
            if list1.val <= list2.val <= list1.next.val:
                list1, list2 = self.insert(list1, list2)
                
            # l2 value is greater than both l1 and l1.next
            # so l1 must be incremented
            elif list2.val > list1.next.val:
                list1 = list1.next
        
        # edge case:
        #   what if we have reached the end of ll1
        #   then insert will append list2 onto ll1
        if not list1.next:
            list1.next = list2
        
        # edge case:
        #    what if we have reached the end of ll2?
        #    -> then we need to increment ll1 until we
        #       find an insert point
        elif not list2.next:
            while list1.next and list1.next.val < list2.val:
                list1 = list1.next
                
            list1,_ = self.insert(list1, list2)
        
        return head
            
    
    def insert(self, list1, list2):
        # note that after we insert, we increment the
        # head of the list
        l1_next, l2_next = list1.next, list2.next
        
        list1.next = list2
        list2.next = l1_next
        
        return list2, l2_next
