
import base64  
str1 = 'djhu1i'
str2 = base64.b64encode(str1.encode())

# print(str2)

import hashlib

str3 = 'djhu1i'

md5 = hashlib.md5()
md5.update(str1.encode())
print(md5.hexdigest())

md6 = hashlib.md5()
md6.update(str3.encode())
print(md6.hexdigest())
