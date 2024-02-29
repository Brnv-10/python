b=int(input("enter a number:"))
a=int(input("enter a number:"))


def calc(onClick):
   if(onClick==1):
    print(a+b)
   elif(onClick==2):
    print(a-b)
   elif(onClick==3):
    print(a*b)
   elif(onClick==4):
    print(a/b)
   else:
    print("Invalid Option")


print("1 for add")
print("2 for sub")
print("3 for mul")
print("4 for div")
onClick=int(input("enter your choice:"))

calc(onClick)
