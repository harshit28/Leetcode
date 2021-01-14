class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        slow,fast = head , head.next
        
        while slow!=fast:
            if not fast or not fast.next:
                return False
                
            slow, fast =  slow.next,fast.next.next
        return True
            
