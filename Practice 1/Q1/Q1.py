import hashlib

inp = "If you want to keep a secret, you must also hide it from yourself"

m1 = hashlib.md5(inp.encode())
dig1 = m1.hexdigest()
print('MD5 full digest : ' + dig1)
print('MD5 full digest size : ' + str(m1.digest_size))
print('MD5 full block size : ' + str(m1.block_size))

inp = "If you want to keep a secret, you must also hide it from yoursel"

m2 = hashlib.md5(inp.encode())
dig2 = m2.hexdigest()
print('MD5 NOT full digest : ' + dig2)
print('MD5 NOT full digest size : ' + str(m2.digest_size))
print('MD5 NOT full block size : ' + str(m2.block_size))
diff = 0
for i in range(len(dig1)):
    if dig1[i] != dig2[i]:
        diff += 1
print('Difference in MD5 : ' + str(diff))

inp = "If you want to keep a secret, you must also hide it from yourself"

m1 = hashlib.sha256(inp.encode())
dig1 = m1.hexdigest()
print('SHA256 full digest : ' + dig1)
print('SHA256 full digest size : ' + str(m1.digest_size))
print('SHA256 full block size : ' + str(m1.block_size))

inp = "If you want to keep a secret, you must also hide it from yourself"

m2 = hashlib.sha256(inp.encode())
dig2 = m2.hexdigest()
print('SHA256 NOT full digest : ' + dig2)
print('SHA256 NOT full digest size : ' + str(m2.digest_size))
print('SHA256 NOT full block size : ' + str(m2.block_size))
diff = 0
for i in range(len(dig1)):
    if dig1[i] != dig2[i]:
        diff += 1
print('Difference in SHA256 : ' + str(diff))
