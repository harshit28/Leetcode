class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tempA,tempB,lenA,lenB=headA,headB,0,0
        while tempA:
            tempA= tempA.next
            lenA+=1
        while tempB:
            tempB= tempB.next
            lenB+=1
            
        if lenA > lenB:
            to_move = lenA-lenB
            while to_move:
                headA=headA.next
                to_move-=1
        else:
            to_move = lenB-lenA
            while to_move:
                headB=headB.next
                to_move-=1
                
        while headA and headB:
            if headA == headB:
                return headA
            headA=headA.next
            headB=headB.next
