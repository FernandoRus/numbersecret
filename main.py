secret = 28

guess = int(input("Find the secret number (between 1 and 30): "))

if guess == secret:
    print("Right! The number is 28!")
else:
    print("Sorry, your guess is not correct... The secret number is not " + str(guess))