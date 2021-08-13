# Given an Array , E.g. [2,5,6,3,9,5,10,56,25] and a number X. now find all the contigous subarrays with length X , if X=3
# then all the subarrays are [2,5,6], [5,6,3], [6,3,9] etc.
# now in all these subarrays find the minimum element.
# and out of all those minimum elements, return the maximum one.

arr = [2, 5, 6, 3, 9, 5, 10, 56, 25]


def max_subarray_num(arr, n=3):
    min_elem = []
    for i, val_i in enumerate(arr):
        slice = arr[i:i+3]
        if len(slice) == 3:
            print(slice)
            min_elem.append(min(slice))
    print(min_elem)
    return max(min_elem)


print(max_subarray_num(arr))


def firstOccurrence(s, x):
    # Write your code here
    found = False
    found_sub_str = []
    for index, i in enumerate(s):
        for j in x:
            if j == i and j:
                found_sub_str.append[j]
