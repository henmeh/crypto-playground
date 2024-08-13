def ggT(number1, number2):
    if type(number1) is int and type(number2) is int:
        remainder = number1 % number2
        if remainder == 0:
            return number2
        return ggT(number2, remainder)
    else:
        raise TypeError("Only integers are allowed")