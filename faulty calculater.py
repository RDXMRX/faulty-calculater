print("1. for Addition")
print("2. for substraction")
print("3. for multiply")
print("4. for divide")
operater = int(input("Enter your choice:"))
n1 = int(input("Enter the first number:"))
n2 = int(input("Enter the second number:"))
if operater==1:
    if n1==56:
        print("Your ans is ",n1 + 50)
    else:
        print("Your ans is ", n1 + n2)   
elif operater==2:
    print("Your ans is ",n1 - n2)
if operater==3:
    if n1==45:
        print("Your ans is ", n1 * 45)
    else:
        print("Your ans is ",n1 * n2)
elif operater==4:
    if n1==56:
        print("Your ans is",n1/66)
    else:
        print("Your ans is ",n1/n2)           
