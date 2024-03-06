choice=int(input("press 1 for celcius to farenheit and 2 for celcius\n"))
value=float(input("enter the value you want to convert\n"))

if(choice==1):
    value= 5/9 * (value - 32)
    print("your value in celcius is:",value)
elif(choice==2):
    value= value* (9/5) +32
    print("the result in farenheit is:", value)
else:
    print("an error occured please reexecute the program. ")