# https://leetcode.com/problems/maximum-subarray/
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Input: nums = [1]
# Output: 1
# Input: nums = [5,4,-1,7,8]
# Output: 23


import math


def max_subarr_approach1(nums):
    "Time complexity o(n³)"
    sum = -math.inf
    # result = {} # {sum: nums}
    for i in range(len(nums)):
        for j in range(len(nums)):
            curr_sum = 0
            # print(nums[i:j+1])
            sub_arr = nums[i:j+1]
            if sub_arr:
                for k in nums[i:j+1]:
                    curr_sum += k
                if curr_sum > sum:
                    # result[curr_sum] = nums[i:j+1]
                    sum = curr_sum
    # max_arr = result[max(result.keys())]
    # max_key = max(result.keys())
    # print(max_key, max_arr)
    print(sum)
                

nums = [-2,1,-3,4,-1,2,1,-5,4]
nums = [-2, -1]
max_subarr_approach1(nums)