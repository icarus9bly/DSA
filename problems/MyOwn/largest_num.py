# Find the largest item in an given array
import math


def largest_pythonic(arr):
    return max(arr)


def largest_by_sort(arr):
    # Brute force
    # Sort the array and then find the number at the last index
    counter = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr


def largest_by_max(arr):
    # Compare and set value of max to larger number
    max_num = arr[0]
    for i in arr:
        if i > max_num:
            max_num = i
    return max_num


arr = [66, 7, 8, 34]
print(largest_pythonic(arr))
print(largest_by_sort(arr))
print(largest_by_max(arr))
