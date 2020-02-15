class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        li=[-1] * len(nums1)
        for i in range(len(nums1)):
            idx =  nums2.index(nums1[i])
            for j in range(idx+1,len(nums2)):
                if nums1[i]<nums2[j]:
                    li[i]=nums2[j]
                    break
        return li
 """ 72ms runtime """
      
