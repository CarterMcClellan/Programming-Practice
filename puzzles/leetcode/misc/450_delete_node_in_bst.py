# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ok how do we want to solve this one?
# 
# finding the node is easy we can just use dfs to find the node
# we we are looking for
#
# but how do we want to handle deletion?
# 
# we can build a recursive function
# root.right = dfs(root.right)
# 
# where the dfs returns None if the key is found
# and otherwise returns a reference to the node
#
# ok so after running this helper we prune the node, but what if the thing we
# removed has children?
# 
# we can just store those children and insert them into the tree
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        child1, child2 = [None], [None]

        def delete_helper(curr: Optional[TreeNode]) -> Optional[TreeNode]:
            if not curr:
                return None
            
            if curr.val == key:
                child1[0] = curr.left
                child2[0] = curr.right
                return None
            
            if curr.left and key < curr.val:
                curr.left = delete_helper(curr.left)
            
            elif curr.right and key > curr.val:
                curr.right = delete_helper(curr.right)
            
            return curr
        
        def insert_helper(curr: Optional[TreeNode], insert_node: TreeNode):
            if not curr:
                return insert_node

            if insert_node.val < curr.val:
                curr.left = insert_helper(curr.left, insert_node)

            elif insert_node.val > curr.val:
                curr.right = insert_helper(curr.right, insert_node)
            
            return curr
            
        root = delete_helper(root)
        if child1[0]:
            root = insert_helper(root, child1[0])
        if child2[0]:
            root = insert_helper(root, child2[0])

        return root