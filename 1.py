
import base64  
str1 = 'djhui'
str2 = base64.b64encode(str1.encode())

print(str2)