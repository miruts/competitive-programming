from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx = 0
        left = 0
        right = len(height) - 1

        while left < right:
            mx = max((min(height[left], height[right]) * (right - left)), mx)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return mx
