# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        currNode = head
        while currNode is not None:
            if currNode in seen:
                return True
            seen.add(currNode)
            currNode = currNode.next
        return False

        