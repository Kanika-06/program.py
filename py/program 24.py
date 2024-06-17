x=int(input("enter the first number:"))
y=int(input("enter the second number:"))
choice=input("enter the choice --A=ADDTION , B=SUBTRACTION , C =MULTIPLICATION, D=DIVISION")
try:
    if choice=="A":
        sum=x+y
        print(sum, "is the sum")
    elif choice=="B":
        difference=x-y
        print(difference, "is the difference")
    elif choice=="C":
        multi=x*y
        print(multi,"is the multiplication")
    elif choice=="D":
        if y!=0:
            div=x/y
            print(div,"is the division")
        else:
            print("ZERO Division ERROR IS NOT ALLOWED")
    else:
        print("INVALID CHOICE")
except ZeroDivisionError:
    print("zero division error is not allowed")