# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        if root is None:
            return True

        def dfs(node):
            nonlocal arr
            if node is None:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        
        dfs(root)
        prev = arr[0]
        for i in range(1, len(arr)):
            if prev >= arr[i]:
                return False
            prev = arr[i]
        return True

        