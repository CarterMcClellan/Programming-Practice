# Here is an example of what you might implement in the scope of an interview
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def create_bin_tree_helper(vals):
#     if not vals: return None
#     mid = len(vals)//2
#     node = TreeNode(vals[mid])
#     node.left = create_bin_tree_helper(vals[:mid])
#     node.right = create_bin_tree_helper(vals[mid+1:])
#     return node

# def create_bin_tree(vals):
#     vals = sorted(vals) # sort values before input
#     root = create_bin_tree_helper(vals)
#     return root

# for convience sake though use https://github.com/joowani/binarytree