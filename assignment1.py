import math
print("\n1. ADDITION\n 2.SUBTRACTION\n 3. MULTIPLICATION \n 4. DIVISION \n 5. MODULUS \n 6. SQRT")
z=int(input("Enter a number of choice : "))
if z==1:
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"+",y,"=",x+y)
elif z==2:
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"-",y,"=",x-y)
elif z==3:
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"*",y,"=",x*y)
elif z==4:
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"/",y,"=",x/y)
elif z==5:
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"%",y,"=",x%y)
elif z==6:
    a=int(input("Enter a number :"))
    print(math.sqrt(a))

