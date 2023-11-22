import random

def choosen_number(x):
    print(f'choose a number between 0 to {x}')
    user_respons = ''
    low = 0
    high = x
    while user_respons != 'yes':
        computer_guess = random.randint(low, high)
        user_respons = input(f'Is your number {computer_guess}?(yes or no) ')
        if user_respons == 'no':
            resp2 = input('lower or higher? ')
            if resp2 == "lower":
                high = computer_guess - 1
            elif resp2 == "higher":
                low = computer_guess + 1
   
    print('yahaha!!!!')

choosen_number(1000)