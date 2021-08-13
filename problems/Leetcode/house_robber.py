# https://leetcode.com/problems/house-robber/
# We build dp[]. Suppose we are at the first house on the block, what is the most money we can make by being here? Well we can rob this house and make that much money, so dp[0] = nums[0]. Suppose we are at the second house on the block, what is the most money we can make by being here? Well we can either rob the first house and not rob the second or we can rob the second and not rob the first. We choose whichever makes us more money, so dp[1] = max(nums[0], nums[1]). Now suppose you are at the ith house, what is the most money we can make by being here? There are 2 cases. Case 1: If we rob the ith house that means we could not have robbed the i - 1th house because they are adjacent, so we could make dp[i - 2] + nums[i]. Case 2: If we dont rob the ith house then we should have robbed the i - 1th. I hope this helped someone.


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
            dp = [0]*len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[len(nums) - 1]
