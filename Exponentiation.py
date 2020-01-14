import time
N = int(input(""))

#Solution 1 - Built-In Power Function

print(pow(2, N))
print("")
print("")

#Solution 2 - String of Integer Calculation

print(str(int(2**N)))
print("")
print("")

#Solution 3 - Bit shifting

print(1 << N)
print("")
print("")

#Solution 4 - Exponentiation by Squaring

def fast_power(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0

    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """

    result = 1
    while power > 0:
        # If power is even
        if power % 2 == 0:
            # Divide the power by 2
            power = power // 2
            # Multiply base to itself
            base = base * base
        else:
            # Decrement the power by 1 and make it even
            power = power - 1
            # Take care of the extra value that we took out
            # We will store it directly in result
            result = result * base

            # Now power is even, so we can follow our previous procedure
            power = power // 2
            base = base * base

    return result
print(fast_power(2, N))

