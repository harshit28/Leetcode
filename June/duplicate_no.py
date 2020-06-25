class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         nums.sort()
        
#         for i in range(len(nums)-1):
#             if nums[i] == nums[i+1]:
#                 return nums[i]
        t=nums[0]
        h=nums[0]
        while True:
            t = nums[t]
            h= nums[nums[h]]
            if t == h:
                break
        t = nums[0]
        while t !=h:
            t = nums[t]
            h = nums[h]
        return h

        
