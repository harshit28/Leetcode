class Solution:
    def totalMoney(self, n: int) -> int:
        output, prev  = 0 ,1
        result = []
        i=1
        while i < n+1 :
            temp=output
            output = temp + 1 
            result.append(output)
            if i % 7 == 0:
               
                output=prev
                prev+=1
                i=0
                n-=7
            i+=1
        return sum(result)
