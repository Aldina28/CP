class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_val = 0
        l=0
        r=len(height)-1
        while l<r:
            area = min(height[l], height[r])*(r-l)
            max_val = max(max_val, area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_val
        

            