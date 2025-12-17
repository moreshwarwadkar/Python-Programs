# Wap to guess the number.

secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct Guess!")
    else:
        print("Wrong! Try again...")
