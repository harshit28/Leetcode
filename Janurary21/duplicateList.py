class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = ListNode(0,head)
        prev = node
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next 
            else:
                prev= prev.next
            head= head.next
        
        return node.next
