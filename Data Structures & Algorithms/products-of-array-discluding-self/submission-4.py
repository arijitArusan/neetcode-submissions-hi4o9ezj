class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        # Step 1: Left products
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]

        # Step 2: Right products
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res