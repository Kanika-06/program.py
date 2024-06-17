n=input("enter the temp you need---celsius or fahrenheit?")
if n=="celsius":
    f=int(input("enter the fahrenheit temp:"))
    c=(f-32)*5/9
    print("the celsius temp is ",c)
else:
    c=int(input("enter the celsius temp:"))
    f=c*(9/5)+32
    print("the fahrenheit temp is ",f)