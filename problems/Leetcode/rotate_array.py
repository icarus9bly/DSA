# https://leetcode.com/problems/rotate-array/
# Given an array, rotate the array to the right by k steps, where k is non-negative.
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]

def rotate(nums, k):
    """ 
    Time complexity: O(n)
    Space complexity: O(n)
    """
    nums.reverse()
    rulo = nums[0:k]
    nulo = nums[k::]
    rulo.reverse()
    nulo.reverse()
    return rulo+nulo

def rotate_neetcode2(nums, k):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    k = k % len(nums) # Set k to 0 is k is eq to len(nums)
    l, r = 0, len(nums)-1
    while r > l:
        nums[l], nums[r] = nums[r], nums[l]
        r-=1
        l+=1
    l, r = 0, k-1
    while r > l:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1
    l, r = k, len(nums)-1
    while r > l:
        nums[l], nums[r] = nums[r], nums[l]
        l+=1
        r-=1    
    return nums

def rotate_neetcode1(nums, k):
    """
    Time complexity: O(n)
    Space complexity: O(n)
    """
    result = [None] * len(nums)
    for i in range(len(nums)):
        diff = (i+k) - (len(nums) - 1)
        if diff > 0:
            result[diff - 1] = nums[i]
        else:
            result[i+k] = nums[i]
    nums = result
    return nums

nums = [1,2,3,4,5,6,7,8]
k = 3
nums = [1,2,3,4,5,6,7]
# Expected: [6,7,8,1,2,3,4,5]
# print(rotate(nums, k))
# print(rotate_neetcode2(nums, 8))
print(rotate_neetcode1(nums, 3))
