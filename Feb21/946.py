class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if len(pushed) != len(popped):
            return False
        pu_len,po_len,i,j = len(pushed),len(popped), 0 , 0 
        temp = []
        while i < pu_len and j < po_len:
            temp.append(pushed[i])
            while temp and temp[-1] == popped[j]:
                temp.pop()
                j+=1
         
            i+=1
        i=len(temp)-1
        
        while j < po_len:
            if temp[i] != popped[j]:
                return False
            i-=1
            j+=1
        return True
