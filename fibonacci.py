# Recursively
def fib(N):
    if N <= 1:
        return N
    else:
        return fib(N-1) + fib(N-2)

# Recursively memoized
def fib_m(N, cache=None):
    if N <= 1:
        return N
    else:
        if cache is None: cache = {}
        if N in cache: return cache[N]
        result=fib(N-1) + fib(N-2)
        cache[N]=result
        return result


# Iteratively
def fib(N):
    if N <= 1:
        return N
    res = [0, 1]
    for i in range(N-1):
        res.append(sum(res[-2:]))
    return res[-1]


print(fib(50))
print(fib_m(50))
