class Solution:
    def binaryTodec(self,s):
       if len(s) == 0:
         return 0
       else:
         return self.binaryTodec(s[0:len(s)-1]) * 2 + int(s[len(s)-1])
    def getDecimalValue(self, head: ListNode) -> int:
        temp,number= head,""
        while temp:
            number += str(temp.val)
            temp= temp.next
        return self.binaryTodec(number)
   
