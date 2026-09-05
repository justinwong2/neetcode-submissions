# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        currNode = head
        while currNode is not None:
            arr.append(currNode)
            currNode = currNode.next
        
        removeIndex = len(arr) - n
        prevNode, afterNode = None, None
        if removeIndex -1 >= 0:
            prevNode = arr[removeIndex - 1]
        if removeIndex + 1 < len(arr):
            afterNode = arr[removeIndex + 1]

        if prevNode is None:
            head = afterNode
        else:
            prevNode.next = afterNode
        return head        