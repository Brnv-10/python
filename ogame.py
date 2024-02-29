import random
guesses=0

top= int(input("enter a number:--"))

if top <=0:
    print("please enter a number greater than zero")
    quit()

rndm=random.randrange(0,16)

while True:
    guesses+=1
    guess=int(input("enter a guess:"))
    if guess > rndm:
        print("you were above the number")
    else:
        print("you were below the number")
    if guess== rndm:
        print("you guessed correct")
        break
    else:
        print("try again")

print('you got it in', guesses, "tries")
