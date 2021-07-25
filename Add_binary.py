def addBinary(a, b):
    """
    With two pointers iterate over both the list of characters
    """
    i = len(a)-1  # 4-1=3
    j = len(b)-1  # 4-1=3
    carry = 0
    res = ""
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            # Increment the carry by adding the num at index going from right to left
            carry += int(a[i])
            i -= 1  # move pointer to left side
        if j >= 0:
            # Increment the carry by adding the num index going from right to left
            carry += int(b[j])
            j -= 1  # move pointer to left side
        # Take the remainder dividing by 2 and store in result string i.e. 1%2=1.
        # Because will have either 0 or 1 in our carry so if 0: 0%2=0, 1: 1%2=1, 2: 2%2=0
        res = str(carry % 2) + res
        carry //= 2  # Divide carry by 2 and round off the quoitent to floor i.e. 1/2=0.5=0
    return res


print(addBinary("1010", "1011"))
