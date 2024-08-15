def ggT(number1, number2):
    if not isinstance(number1, int) and isinstance(number2, int):
        raise TypeError("Only integers are allowed")
    else:
        remainder = number1 % number2
        if remainder == 0:
            return number2
        return ggT(number2, remainder)
    

def eea(number1, number2):
    if not isinstance(number1, int) and isinstance(number2, int):
        raise TypeError("Only integers are allowed")
    else:
        if number1 == 0:
            return number2, 0, 1
        else:
            ggt, s1, t1 = eea(number2 % number1, number1)

            s = t1 - (number2 // number1) * s1
            t = s1
    
    return ggt, s, t


def mod_inverse(number1, modulo):
    if not isinstance(number1, int) and isinstance(modulo, int):
        raise TypeError("Only integers are allowed")
    else:
        ggt, s, _ = eea(number1, modulo)

        if ggt !=1:
            raise ValueError("No modular inverse")
        
        return s % modulo