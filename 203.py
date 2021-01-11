class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        record = prev
        ptr = head
        
        while ptr:
            if ptr.val==val:
                prev.next = ptr.next
                ptr = prev.next
            else:
                prev = ptr
                ptr = ptr.next
                
        return record.next
