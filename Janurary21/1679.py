class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        hashmap = {}
        i=0
        operation = 0 
        for i in range(len(nums)):
            if nums[i] < k:
                if nums[i] in hashmap:
                    operation+=1
                    if hashmap[nums[i]] == 1:
                        del hashmap[nums[i]]
                    else:
                        hashmap[nums[i]]-=1
                else:
                    val=hashmap.get(k-nums[i],0)
                    hashmap[k-nums[i]] = val + 1
        return operation
