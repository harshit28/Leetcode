class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count,i=0,0
        n = len(nums)
        while i <= n-2:
            if nums[i] == nums[i+1] and count >= 1:
                nums.pop(i)
                n-=1
                i-=1
            elif nums[i] == nums[i+1]:
                count+=1
            else:
                count=0
            i+=1
        return len(nums)
