class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        l,h=0,len(citations)-1
        n=len(citations)
        while l<=h:
            mid = (h+l)//2
            if citations[mid] >= n - mid:
                h = mid-1
            else:
                l = mid+1
        return n-l 
        
