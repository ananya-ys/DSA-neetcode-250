class Solution:
    def trap(self, height):
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n
        # build leftMax
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        # build rightMax
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        water = 0
        # calculate trapped water
        for i in range(n):
            trapped = min(leftMax[i], rightMax[i]) - height[i]
            water += trapped
        return water