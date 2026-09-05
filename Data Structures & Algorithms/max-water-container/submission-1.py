class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) < 2:
            return 0
        left = 0
        right = len(heights) - 1
        ans = 0
        while left < right:
            currArea = (right - left) * min(heights[left], heights[right])
            ans = max(ans, currArea)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return ans
            
        
        