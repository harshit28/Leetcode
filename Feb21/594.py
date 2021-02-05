class Solution:
    def findLHS(self, nums: List[int]) -> int:
        hashmap = Counter(nums)
    
        
        
        result=0
        for elem in hashmap:
            if elem+1 in hashmap:
                result = max(result,hashmap[elem+1] + hashmap[elem])
        return result
        
