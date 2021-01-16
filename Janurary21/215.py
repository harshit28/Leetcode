class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap=[]
        for num in nums:
            heapq.heappush(heap,num)
        index,smallest=0,len(nums)-k
        
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
            
        return heapq.heappop(heap)
