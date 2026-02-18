class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lista = headA
        listb = headB

        while lista != listb:
            #When a pointer reaches the end of one list and switches to the other, the difference in lengths between the two lists is neutralized. This ensures that both pointers traverse the same total distance before meeting.
            lista = lista.next if lista else headB
            listb = listb.next if listb else headA
        
        return listb