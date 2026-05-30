# simple calculator in python 
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))

print("\n   OPERATORS   ")
print("+ Adition        ")
print("- Substitution   ")
print("x Multiplication ")
print("/ Division       ")
print("% Modulo Division")

choice=input("Enter symbols for calculation:")
    
if choice=="+":
     print(f"{a}+{b}=",a+b)
        
elif choice=="-":
     print(f"{a}-{b}=",a-b)
        
elif choice=="x":
     print(f"{a}x{b}=",a*b)
    
elif choice=="/":
     print(f"{a}/{b}=",a/b)
    
elif choice=="%":
     print(f"{a}%{b}=",a%b)
        
else:
     print("invalid operator plz choose +,-,x,/,%")
