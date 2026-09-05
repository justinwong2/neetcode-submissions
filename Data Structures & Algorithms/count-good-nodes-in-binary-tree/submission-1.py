# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        if root is None:
            return 0
        currHighest = root.val
        def dfs(node, prevHighest):
            if node is None:
                return None
            nonlocal count
            nonlocal currHighest
            currHighest = max(currHighest, node.val)
            if node.val >= currHighest:
                count += 1
            dfs(node.left, currHighest)
            dfs(node.right, currHighest)
            currHighest = prevHighest
        
        dfs(root, root.val)
        return count



        