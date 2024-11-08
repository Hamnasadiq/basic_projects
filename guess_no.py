import random
random_no=random.randint(1,100)
attempts=0
while attempts<4:
    user_guess=int(input("Your guess: "))
    attempts+=1
    if user_guess>random_no:
        print("Your guess is high.")
    elif user_guess<random_no:
       print("Your guess is low.") 
    else:
       print("Your guess is correct ")   