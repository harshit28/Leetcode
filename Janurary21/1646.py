class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        
        if n < 2:
            return n
        
        nums,i=[0,1] + [0] * (n-1),1
        while i < n+1:
            if  2  <= 2 * i <= n: 
                nums[2*i] = nums[i]
            if 2 <= 2 * i + 1 <= n:
                nums[2*i+1] =nums[i] + nums[i + 1]
            i+=1
            
        return max(nums)
