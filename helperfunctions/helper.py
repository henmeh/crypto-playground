def ggT(number1, number2):
    if number1 <= number2:
        raise ValueError("First number must be bigger than second number")
    elif not isinstance(number1, int) and isinstance(number2, int):
        raise TypeError("Only integers are allowed")
    else:
        remainder = number1 % number2
        if remainder == 0:
            return number2
        return ggT(number2, remainder)