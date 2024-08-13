import rsa

(pub_key, priv_key) = rsa.newkeys(512)

x = b"Hallo Welt"
y = rsa.encrypt(x, pub_key)

print(f"Klartext: {x}")
print(f"Chiffrat: {y}")

x_decrypted = rsa.decrypt(y, priv_key)

print(f"Entschlüsselter Klartext: {x_decrypted}")