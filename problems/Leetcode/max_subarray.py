# https://leetcode.com/problems/maximum-subarray/
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Input: nums = [1]
# Output: 1
# Input: nums = [5,4,-1,7,8]
# Output: 23


import math


def max_subarr_cubic(nums):
    "Time complexity o(n³)"
    max_sum = -math.inf
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr_sum = 0
            sub_arr = nums[i:j+1]
            for k in sub_arr:
                curr_sum += k
            if curr_sum > max_sum:
                max_sum = curr_sum
    print(f'max_subarr_cubic : {max_sum}')
                
def max_subarr_internet_cubic(nums):
    n = len(nums)
    max_sum = -10000    
    for left in range(0, n):
        for right in range(left, n):
            window_sum = 0
            for k in range(left, right + 1):
                window_sum += nums[k]
            max_sum = max(max_sum, window_sum)
    print(f'max_subarr_internet_cubic : {max_sum}')
        
def max_subarr_quadratic(nums):
    "Time complexity o(n²)"
    max_sum = -math.inf
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i,len(nums)):
            curr_sum += nums[j]
            if curr_sum > max_sum:
                max_sum = curr_sum
    print(f'max_subarr_quadratic : {max_sum}')

def max_subarr_internet_quadratic(nums):
    n = len(nums)
    max_sum = -1000000000
    for left in range(0, n):
        running_sum = 0
        for right in range(left, n):
            running_sum += nums[right]
            max_sum = max(max_sum, running_sum)
    print(f'max_subarr_internet_quadratic : {max_sum}')

def max_subarr_linear(nums):
    """
    We are inspecting the item at index i.
    We want to answer the question:
    "What is the Max Contiguous Subarray Sum we can achieve ending at index i?"
    We have 2 choices:
    maxEndingHere + nums[i] (extend the previous subarray best whatever it was)
      1.) Let the item we are sitting at contribute to this best max we achieved
      ending at index i - 1.
    nums[i] (start and end at this index)
      2.) Just take the item we are sitting at's value.
    The max of these 2 choices will be the best answer to the Max Contiguous
    Subarray Sum we can achieve for subarrays ending at index i.
    Example:
    index     0  1   2  3   4  5  6   7  8
    Input: [ -2, 1, -3, 4, -1, 2, 1, -5, 4 ]
             -2, 1, -2, 4,  3, 5, 6,  1, 5    'maxEndingHere' at each point
    The best subarrays we would take if we took them:
      ending at index 0: [ -2 ]           (snippet from index 0 to index 0)
      ending at index 1: [ 1 ]            (snippet from index 1 to index 1) [we just took the item at index 1]
      ending at index 2: [ 1, -3 ]        (snippet from index 1 to index 2)
      ending at index 3: [ 4 ]            (snippet from index 3 to index 3) [we just took the item at index 3]
      ending at index 4: [ 4, -1 ]        (snippet from index 3 to index 4)
      ending at index 5: [ 4, -1, 2 ]     (snippet from index 3 to index 5)
      ending at index 6: [ 4, -1, 2, 1 ]  (snippet from index 3 to index 6)
      ending at index 7: [ 4, -1, 2, 1, -5 ]    (snippet from index 3 to index 7)
      ending at index 8: [ 4, -1, 2, 1, -5, 4 ] (snippet from index 3 to index 8)
    Notice how we are changing the end bound by 1 everytime.
    """    
    max_so_far = nums[0]
    max_ending_here = nums[0]
    for i in range(1, len(nums)):
        max_ending_here = max_ending_here + nums[i]     
        if max_ending_here < nums[i]:
            max_ending_here = nums[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    print(f"max_subarr_linear : {max_so_far}")

nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [-2, -1]
max_subarr_cubic(nums)
max_subarr_internet_cubic(nums)
max_subarr_quadratic(nums)
max_subarr_internet_quadratic(nums)
max_subarr_linear(nums)