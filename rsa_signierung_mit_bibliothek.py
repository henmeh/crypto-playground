import rsa

(pub_key, priv_key) = rsa.newkeys(512)

x = b"Hallo Welt"

signature = rsa.sign(x, priv_key, "SHA-256")
print(rsa.verify(x, signature, pub_key))

x_new = b"Hello Welt"
print(rsa.verify(x_new, signature, pub_key))
