import math
print("\n1. ADDITION\n 2.SUBTRACTION\n 3. MULTIPLICATION \n 4. DIVISION \n 5. MODULUS \n 6. SQRT")
z=int(input("Enter a number of choice : "))
def add():
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"+",y,"=",x+y)
def sub():
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"-",y,"=",x-y)
def mul():
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"*",y,"=",x*y)
def div():
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"/",y,"=",x/y)
def mod():
    x=int(input("Enter num :"))
    y=int(input("Enter a num2: "))
    print(x,"%",y,"=",x%y)
def sqrt():
     a=int(input("Enter a number :"))
     print(math.sqrt(a))
    
if z==1:
    add()
elif z==2:
    sub()
elif z==3:
    mul()
elif z==4:
    div()
elif z==5:
   mod()
elif z==6:
    sqrt()
