#This is the code for calculator
a = int(input("enter any number"))
b = int(input("enter any number"))

c = int(input("enter the operator"))

if c == 1:
    print(a+b)
if c==2:
    print(a*b)
if c==3:
    print(a-b)
if c==4:
    print(a/b)
else:
    print("no operation")
    