# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far): 
            if not node: 
                return 0 
            is_good = 0 
            if node.val >= max_so_far: 
                is_good = 1
                max_so_far = node.val

            left_good_nodes = dfs(node.left, max_so_far)
            right_good_nodes = dfs(node.right, max_so_far)

            return is_good + left_good_nodes + right_good_nodes

        return dfs(root, root.val)

        
        