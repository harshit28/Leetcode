class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        s = []
        for i, x in enumerate(nums):
            while s and s[-1] > x and len(s) + n - i > k:
                s.pop()
            if len(s) < k:
                s.append(x)
        return s
    
