class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ptr = head
        length = 0
        while head:
            head= head.next
            length+=1
        
        index = length - n
        if index == 0 :
            head = t_p= ptr
            if head.next:
                     head = head.next
                     return head
            else:
                    return None
        temp_i = 1
        head = tp = ptr
        while head:
            if temp_i == index:
                head.next = head.next.next
            head = head.next
            temp_i+=1
        return tp
