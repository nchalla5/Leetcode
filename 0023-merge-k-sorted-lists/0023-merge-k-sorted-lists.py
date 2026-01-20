# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = ListNode(0)
        prev = merged
        k = len(lists)
        counter = count()
        heap = []
        for lst in lists:
            if lst:
                heap.append((lst.val, next(counter), lst))
        # print(heap)
        heapq.heapify(heap)
        while(len(heap) > 0):
            mini = heapq.heappop(heap)[2]
            if mini.next:
                heapq.heappush(heap, (mini.next.val, next(counter), mini.next))
            prev.next = mini
            prev = mini
        return merged.next