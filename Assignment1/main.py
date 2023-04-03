import random
import string

length = int(input("Enter the length of passsword: "))
nums = int(input("Enter the number of password to be generated: "))

str = string.ascii_letters+ string.digits

for i in range(nums+1):
    strr=''
    for j in range(length):
       strr=''.join(random.choice(str))
    print(str)