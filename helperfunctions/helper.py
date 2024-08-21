import random

def ggT(number1, number2):
    if not isinstance(number1, int) or not isinstance(number2, int):
        raise TypeError("Only integers are allowed")
    else:
        while number2 != 0:
            number1, number2 = number2, number1 % number2
        return number1
    

def eea(number1, number2):
    if not isinstance(number1, int) or not isinstance(number2, int):
        raise TypeError("Only integers are allowed")

    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = number1, number2

    while r1 != 0:
        quotient = r0 // r1

        # Update remainders
        r0, r1 = r1, r0 - quotient * r1

        # Update s and t
        s0, s1 = s1, s0 - quotient * s1
        t0, t1 = t1, t0 - quotient * t1

    return r0, s0, t0


def mod_inverse(number1, modulo):
    if not isinstance(number1, int) or not isinstance(modulo, int):
        raise TypeError("Only integers are allowed")
    else:
        ggt, s, _ = eea(number1, modulo)

        if ggt !=1:
            raise ValueError("No modular inverse")
        
        return s % modulo
    

def miller_rabin_test(n, k=5):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform the test k times
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True