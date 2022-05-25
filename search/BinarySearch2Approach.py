def binary_search_recursive(arr, target):
    """
    Find if the target exists in arr and return num if exists
    """
    low = 0
    high = len(arr) - 1
    if high == low:
        return arr[high]
    mid = (low + high) // 2
    if arr[mid] > target:
        return binary_search_recursive(arr[low:mid], target)
    else:
        return binary_search_recursive(arr[mid+1:high+1], target)

def binary_search_recursive_internet(array, x, low, high):
    """
    Find if the target exists in arr and return index of num
    """    
    if high >= low:
        mid = low + (high - low)//2
        # If found at mid, then return it
        if array[mid] == x:
            return mid
        # Search the left half
        elif array[mid] > x:
            return binary_search_recursive_internet(array, x, low, mid-1)
        # Search the right half
        else:
            return binary_search_recursive_internet(array, x, mid + 1, high)
    else:
        return -1
def binary_search_iterative(arr, target):
    """
    Find if the target exists in arr and return index of num
    """    
    low = 0
    high = len(arr)-1
    while high >= low:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

arr = [-789, -89, 0, 1, 77, 890, 999, 1000, 1001, 1002, 10003, 555555]
# arr = [i+1 for i in range(1000)]
print(binary_search_iterative(arr, 77))
print(binary_search_recursive(arr, 77))
print(binary_search_recursive_internet(arr, 77, 0, len(arr)-1))