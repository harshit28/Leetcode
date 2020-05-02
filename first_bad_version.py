
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l,h=0,n
        while l<h:
            mid = l+(h-l)//2
            if not isBadVersion(mid):
                l=mid+1
            else:
                h=mid
        return l       
