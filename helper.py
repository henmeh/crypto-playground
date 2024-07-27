def ggT(a, b):
    c = a % b
    if c == 0:
        return b
    return ggT(b, c)

def eea(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x1, y1 = eea(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return (gcd, x, y)