class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        count = 0 
        unique=0
        for num in nums:
            if num == 1:
                if count < k and unique!=0:
                    return False
                count = 0
                unique+=1
            else:
                count+=1
        return True
