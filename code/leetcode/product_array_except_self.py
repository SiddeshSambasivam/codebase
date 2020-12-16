# Problem: https://leetcode.com/problems/product-of-array-except-self/
# Trick:
# 1. Divide the element at each postion from the array and multiply
# 2. split into two and calculate

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 1, 2, 3, 4
        # 1, 1, 2, 6
        # 24, 12, 4, 1

        forward = [1 for _ in range(len(nums))]
        rev = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):

            forward[i] = nums[i-1] * forward[i-1]

        for j in range(0, len(nums)-1):

            rev[len(nums)-2-j] = nums[len(nums)-1-j] * rev[len(nums)-1-j]

        result = []
        for f, r in zip(forward, rev):

            result.append(f*r)

        return result


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # 1,2,3,4
        # 1,1,2,6

        # 3,2,1,0
        # 6,2,1,1

        # r = 1
        # result[i] = result[i] * r
        # r = r * nums[i]

        result, r = [1]*len(nums), 1
        for i in range(1, len(nums)):

            result[i] = result[i-1] * nums[i-1]

        for i in reversed(range(len(nums))):

            result[i] = result[i] * r
            r = r * nums[i]

        return result
