from typing import Optional 

"""
Couple of important realizations here
1) append and pop from a list are O(1) in python, you don't need to write a linked list
2) The tricky bit of this problem is how do you maintain the min when you are popping 
   from the list

The solution is to maintain a prefix list of the mins, so essential you know what 
the min will be after you pop
"""

class Node:
    def __init__(self, val: int, next_node: Optional['Node']):
        self.val = val
        self.next_node = next_node

class MinStack:
    def __init__(self):
        self.top_node = None
        self.smallest_node = None

    def push(self, val: int) -> None:
        # update the top node
        if self.top_node:
            new_node = Node(val=val, next_node=self.top_node)
            self.top_node = new_node
        else:
            new_node = Node(val=val, next_node=None)
            self.top_node = new_node

        # maintain a prefixed list of the smallest nodes
        if self.smallest_node:
            min_val = min(val, self.smallest_node.val)
            new_node = Node(val=min_val, next_node=self.smallest_node)
            self.smallest_node = new_node
        else:
            new_node = Node(val=val, next_node=None)
            self.smallest_node = new_node            

    def pop(self) -> None:
        if self.top_node:
            self.top_node = self.top_node.next_node

        if self.smallest_node:
            self.smallest_node = self.smallest_node.next_node

    def top(self) -> int:
        if self.top_node:
            return self.top_node.val

        return -1

    def getMin(self) -> int:
        if self.smallest_node:
            return self.smallest_node.val

        return -1