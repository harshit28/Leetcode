class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n,output = len(nums)+1 , []
        sn=set(nums)
        
        total,currenttotal,settotal = n*(n-1) //2 , sum(nums), sum(sn)
        
        output.append(currenttotal- settotal)
        output.append(total-settotal)
        
        return output
