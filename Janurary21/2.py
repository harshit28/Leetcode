class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ptr = newList = ListNode(None)
        
        number1,number2 = "" ,""
        
        while l1:
            number1+=str(l1.val)
            l1=l1.next
            
        while l2:
            number2+=str(l2.val)
            l2=l2.next
        
        output = int(number1[::-1]) + int(number2[::-1])
        output = str(output)[::-1]
        for char in output:
            node = ListNode(char,None)
            newList.next= node
            newList = newList.next
            
        return ptr.next
