# create simple password prj in python 
import random 

length=int(input("Enter length of ur password: "))
password=""
char="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@"

for i in range(length):
    password+=random.choice(char)
 
print("Generated password:",password)   
