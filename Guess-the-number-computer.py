import random

def guess(x):
    number_rand = random.randint(0, x)
    guess = 0
    while guess != number_rand:
        guess = int(input(f'guess a number between 0 to {x}: '))
        if guess < number_rand:
            print('Too low, Try again')
        elif guess > number_rand:
            print('Too high, Try again')
    print(f'Exactly, the number is {number_rand}')

guess(10)