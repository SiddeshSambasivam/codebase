# Problem: https://leetcode.com/problems/container-with-most-water/
# Trick:
# 1. Use two pointers to track the trade off between width and height

class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Time complexity: O(n)
        left, right = 0, len(height)-1
        max_area = (right - left) * min(height[left], height[right])

        while left < right:

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

            local_area = (right - left) * min(height[left], height[right])

            if local_area > max_area:
                max_area = local_area

        return max_area

    def naive(self, height: List[int]) -> int:

        # Time complexity: O(n^2)

        max_ = 0
        for i in range(len(height)):

            for j in range(i+1, len(height)):

                b = (j-i)
                l = min(height[i], height[j])
                if l*b >= max_:
                    max_ = l*b

        return max_
