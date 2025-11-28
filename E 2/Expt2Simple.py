# -*- coding: utf-8 -*-
import hashlib 

M = input("Enter message: ")
Digest = hashlib.sha256(M.encode()).hexdigest()
print(M)
print(Digest)

M = M + " "
Digest = hashlib.sha256(M.encode()).hexdigest()
print(Digest)
