# Guess the Number

target_number = 10
user_number = int(input("Enter your guess: "))

if user_number > target_number:
    print("Too high")
elif user_number < target_number:
    print("Too low")
else:
    print("Correct! You guessed the number 10")