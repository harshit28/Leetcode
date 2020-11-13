class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        output=[]
        
        def backtrack(nums,l,r):
            if l == r:
                array = nums[::]
                if array not in output:
                     output.append(array)
                return
                
            for i in range(l,r):
                nums[i],nums[l] = nums[l],nums[i]
                backtrack(nums,l+1,r)
                nums[i],nums[l] = nums[l],nums[i]
        backtrack(nums,0,len(nums))
        return output
