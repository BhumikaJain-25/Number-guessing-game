import random

# r=random.randrange(-1,11)#doesnot generate 11 it goes to 10
# print(r)

# r=random.randint(-1,11)#include 11 as well
# print(r)
user_no=input("Type a number range:")
if user_no.isdigit():
    user_no=int(user_no)
    if user_no<=0:
        print("please type a number greater then zero ")
        quit()
else:
    print("Please type a number next time")
    quit()

random_number=random.randint(0,user_no)
guesses=0
# print(random_number)
while True:
    guesses+=1
    user_guess=input(" try to guess :")
    if user_guess.isdigit():
        user_guess=int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess==random_number:
        print("you got it!!!!")
        break
    
    elif user_guess>random_number:
        print("you are above the no")
    else:
        print("you are below the no , better luck next time!!!")

print(f"You got it in {guesses} guesses.")