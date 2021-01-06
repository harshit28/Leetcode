class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        hashset,count = set(arr)    ,0 
        max = 100000
        for elem in range(1,max):
            if elem not in hashset:
                count+=1
            if count == k:
                return elem
