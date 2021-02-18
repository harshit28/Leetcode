class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        
        dp, sum = 0 ,0 
        
        for i in range(2,len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp+=1
                sum+=dp
            else:
                dp = 0
        return sum
        
