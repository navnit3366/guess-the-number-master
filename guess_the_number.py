from random import randint

TARGET = randint(0, 100)
GUESSES = []
TRIES = 0

intro = '''
WELCOME TO GUESS THE NUMBER!
I'm thinking of a number between 1 and 100
If your guess is more than 10 away from my number, I'll tell you you're COLD
If your guess is within 10 of my number, I'll tell you you're WARM
If your guess is farther than your most recent guess, I'll say you're getting COLDER
If your guess is closer than your most recent guess, I'll say you're getting WARMER
LET'S PLAY!
'''
print(intro)

while True:
    guess = int(input("Enter a Number: "))

    if guess > 99 or guess < 1:
        print('OUT OF BOUNDS')
        continue

    TRIES += 1

    if guess == TARGET:
        break
    elif TRIES == 1:
        if abs(TARGET - guess) <= 10:
            print('WARM')
        else:
            print('COLD')
    else:
        if abs(TARGET-guess) > abs(TARGET-GUESSES[-1]):
            print('COLDER!')
        else:
            print('WARMER!')

    GUESSES.append(guess)

print(f'\nYou guessed {TARGET} in {TRIES} tires\n')
input('Press Enter To Exit')
