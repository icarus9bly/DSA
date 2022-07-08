# Quesion 1 Return smallest possible integer that does not exists in A
# Quesion 2 Find the smallest positive number missing from an unsorted array | Set 1
# Quesion 3 https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

def smallest_positive_integer_with_sort(A):
    """
    Time: O(nlogn * n) because of sort
    Space: O(1)
    """
    smallest_int = 1
    A.sort()
    for i in A:
        if smallest_int == i:
            smallest_int += 1
        if smallest_int < i:
            return smallest_int
    return smallest_int

def smallest_positive_integer_with_set(A):
    """
    Time: O(n) = O(1) * n because for sets fetching key is O(1) 
    Space: O(n)
    """
    A = set(A)
    s_i = 1
    # solution set will be {1..len(A)+1}
    for _ in range(len(A)):
        if s_i in A:
            s_i += 1
        else:
            return s_i
    return s_i

def smallest_positive_integer_without_set():
    pass

A = [1,3,6,4,2] # Output: 5
A = [1,2] # Output: 3
A = [1,20,21] # Output: 2
print(smallest_positive_integer_with_sort(A))
print(smallest_positive_integer_with_set(A))

