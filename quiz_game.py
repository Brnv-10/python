print("welcome to my quiz game  ")

playing=input("do you want to play  ")
socre=0
 
if playing != "yes":
    quit()

print("okay!! lets begin the game.")


answer= input("who is the prime minister of India")
if answer == "Narendra Modi":
    print("correct")
    socre+=1
else:
    print("incorrect! the correct answer is Narendra Modi")


answer= input("who is the chief minister of Assam")
if answer == "hemanta Bishwa Sharma":
    print("correct")
    socre+=1
else:
    print("incorrect! the correct answer is Hemanta BIShwa Sharma")


answer= input("are you a human")
if answer == "yes":
    socre+=1
    print("correct")
else:
    print("incorrect! ")


answer= input("is 1+1==2")
if answer == "yes":
    print("correct")
    socre+=1
else:
    print("incorrect! the answer is yes")
    
print("you got " + str(socre) + "questions correct.")





