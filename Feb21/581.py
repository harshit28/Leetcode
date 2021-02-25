class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        i,j= 0,len(nums)-1
        s_nums=sorted(nums)
        
        while i <= j and s_nums[i]  == nums[i]:
                    i+=1
        while j > 0 and s_nums[j]   == nums[j]:
                     j -=1
         
        return 0 if i > j else (j - i) + 1
