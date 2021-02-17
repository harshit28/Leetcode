class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right,area = 0 , len(height) -1 , 0
        
        if len(height) <= 1:
            return 0
        
        while left < right:
            minh = min(height[left],height[right])
            dist = right - left
            area = max(area,dist * minh)
            
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return area
