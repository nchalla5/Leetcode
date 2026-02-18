# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def removeNode(head, k):
            if head is None:
                return
            removeNode(head.next, k)
            k[0] += 1
            if k[0] == n:
                head.next = head.next.next
            return
        k = [-1]
        removeNode(head, k)
        if k[0] == n-1:
            return head.next
        return head

                
        