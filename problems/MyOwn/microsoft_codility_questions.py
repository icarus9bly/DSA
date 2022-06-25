# Quesion 1 Return smallest possible integer that does not exists in A
# Quesion 2 Find the smallest positive number missing from an unsorted array | Set 1
# Quesion 3 https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

def smallest_positive_integer(A):
    s = 1
    for i in A:
        if s == i:
            s=s+1
        if s > A:



A = [1,3,6,4,1,2] # Output: 5
smallest_positive_integer(A)

