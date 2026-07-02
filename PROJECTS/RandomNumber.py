import math
import random

low=1
high=10
answer=random.randint(low,high)

tryes=0
isRun=True

while isRun:
    guess=input('Enter Number :')
    if guess.isdigit():
        guess=int(guess)
        tryes +=1
        if guess<answer:
            print('Too Lower:')
        elif guess>answer:
            print('Too Higer')
        else:
            print(f"Corect! The Answer is {answer}")
            print(f'Number of tryes is {tryes}')
            isRun=False
    else:
        print("Enter valies number not Sring Use")