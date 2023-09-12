import random

def Guess_number(x):
    random_number=random.randint(1,x)
    guess=0
    while guess != random_number:
        guess=int(input(f"Guess the number between 1 and {x} : "))
        if guess<random_number:
            print("Sorry, Too Low try again")
        elif guess>random_number:
            print("Sorry, Too High try again ")

    print(f"Congratulations, you knew right. The number was {random_number}")
            
Guess_number(10)