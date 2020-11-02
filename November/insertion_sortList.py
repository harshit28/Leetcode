class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        some_head= ListNode()
        
        temp=head
        while temp:
            curr = some_head
            nex = curr.next
            while nex:
                if temp.val < nex.val:
                    break
                curr = nex
                nex = nex.next
            nex_iter = temp.next
            temp.next = nex
            curr.next = temp
            
            temp = nex_iter
        return some_head.next
