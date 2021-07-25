# Recursively
def fib(N):
    if N <= 1:
        return N
    else:
        return fib(N-1) + fib(N-2)


# Iteratively
def fib(N):
    if N <= 1:
        return N
    res = [0, 1]
    for i in range(N-1):
        res.append(sum(res[-2:]))
    return res[-1]


print(fib(50))
