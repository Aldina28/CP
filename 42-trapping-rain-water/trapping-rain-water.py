class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_left = height[l]
        max_right = height[r]
        area = 0
        while l<r:
            if height[l]<height[r]:
                if height[l]>max_left:
                    max_left = height[l]
                else:
                    area += max_left - height[l]
                l+=1
            else:
                if height[r]>max_right:
                    max_right = height[r]
                else:
                    area += max_right - height[r]
                r-=1
        return area