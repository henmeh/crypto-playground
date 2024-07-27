from helper import ggT, eea
# public key: (e,n)
# private key (d,n)
# klartext: x
# chiffrat: y
# verschlüsselung: y = pow(x, e, n)
# entschlüsselung: x = pow(y, d, n)

# RSA Schlüsselerzeugung (Set-Up Phase)
# ----------------------------------------

# 1: Wähle zwei Primzahlen
p = 3
q = 11

# 2: Berechne n = p * q
n = p * q

# 3: Berechne phi(n) = (p - 1) * (q - 1)
phi = (p - 1) * (q - 1)

# 4: Wähle e in {1, 2, ... phi(n) - 1}, so dass ggT(e, phi(n)) = 1
e = 3
print(f"ggT(e, phi): {ggT(e, phi)}")

# 5: Berechne privaten Schlüssel d so dass d * e = 1 mod phi(n)
d = eea(e, phi)[1]
print(f"private key: {d}")

# 6: Verschlüsselung
x = 4
print(f"Klartext: {x}")
y = pow(x, e, n)
print(f"Chiffrat: {y}")

# 7: Entschlüsselung:
x = pow(y, d, n)
print(f"Entschlüsselter Klartext: {x}")

