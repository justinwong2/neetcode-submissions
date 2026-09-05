# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        highest = root.val

        #can i not do post order traversal here? i go left, i keep track of the left branch highest, i go right, i keep track of the right branch highest, then i either add the curr node value and compare against the highest, or i return the max of both paths + my current node
        def dfs(node):
            if node is None:
                return 0
            nonlocal highest
            left = dfs(node.left)
            right = dfs(node.right)
            highest = max(highest, left + right + node.val, left + node.val, right + node.val, node.val)
            return max(node.val + left, node.val + right, node.val)
        
        dfs(root)
        return highest