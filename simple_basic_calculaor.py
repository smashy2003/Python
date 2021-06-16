#additon
def add(a,b):
    print("Addition of",a,"and",b,"is",a+b)
    start()
#subtraction
def sub(a,b):
    print("Subtraction of",a,"and",b,"is",a-b)
    start()
#multiplication
def prd(a,b):
    print("Product of",a,"and",b,"is",a*b)
    start()
#division
def div(a,b):
    if b==0:
        print("Second number must not be zero on division")
        start()
    else:
        print("Division of",a,"and",b,"is",a/b)
        start()
#modular division
def mdiv(a,b):
    if b==0:
        print("Second number must not be zero on division")
    else:
        print("Modular division of",a,"and",b,"is",a%b)
        start()
#start
def start():
    print("Python Calculator\nChoose any option\n\t\t1.Add\n\t\t2.Subtract\n\t\t3.Product\n\t\t4.Division\n\t\t5.Modular Division\n\t\t6.Exit")
    n=int(input("Enter the option:"))
    if n<=5:
       n1=int(input("Enter first number:"))
       n2=int(input("Enter the second number:"))
    if n==1:
       add(n1,n2)
    if n==2:
       sub(n1,n2)
    if n==3:
       prd(n1,n2)
    if n==4:
       div(n1,n2)
    if n==5:
       mdiv(n1,n2)
    if n==6:
       pass
    if n>6:
       print("Invalid Option\n\n")
       start()
start()
