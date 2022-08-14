# See factorial Recursion in factorial_recursion.png
def factorial(num):
    # Base Case
    # 1!=1
    if num == 1:
        return 1
    # Recursive case
    # 5!=5*4*3*2*1=5*4! or n*(n-1)!
    return num*factorial(num-1)


print(factorial(5))
print(factorial(998))