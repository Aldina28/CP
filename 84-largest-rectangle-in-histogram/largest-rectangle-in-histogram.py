class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        area = 0
        stack = [-1]
        for i in range(len(heights)):
            while heights[i]<heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i-stack[-1]-1
                area = max(area, height*width)
            stack.append(i)
        return area    