# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        q = deque()
        ans = []
        if root is None:
            return ans
        q.append(root)

        while q:
            temp = []
            for i in range(0, len(q)):
                currNode = q.popleft()
                temp.append(currNode.val)
                if currNode.left is not None:
                    q.append(currNode.left)
                if currNode.right is not None:
                    q.append(currNode.right)
            ans.append(temp)
        return ans

        
        