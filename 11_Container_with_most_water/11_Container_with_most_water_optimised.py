# Two pointer approach: O(n) time complexity, O(1) space complexity

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_vol = 0

        while left < right:
            vol = (right - left) * min(heights[left], heights[right])
            max_vol = max(max_vol, vol)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_vol
        