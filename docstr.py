n=int(input("enter the value of n"))
def square(n):
    '''this function takes value of n and returns the square of n'''
    n=n**2
    
print(square.__doc__)
square(n)
print(n)

#doc strings are written under the head of a function and they can contain any defintion about the function and can be printed later