from itertools import combinations 
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
            n = len(nums)
            subset=[]
            for i in range(n+1):
                sub=list(combinations(nums,i))
                for s in sub:
                    subset.append(s)
            return subset
