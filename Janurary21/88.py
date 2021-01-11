class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        if nums1 and not nums2:
            return 
        i = 0
        
        while i <= m and n:
            if nums2[0] <= nums1[i]:
                nums1.pop()
                nums1.insert(i,nums2[0])
                nums2.pop(0)
                m+=1
                n-=1
            i+=1
            
        for _ in range(n):
            nums1.pop()
            
        while n:
            nums1.append(nums2.pop(0))
            n-=1
