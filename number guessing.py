# number guessing
import random
lowest_num = 1
highest_num = 100
guesses = 0
is_running = True 
answer = random.randint(lowest_num, highest_num)

print("Welcome to game number guessing")
print(f"Select number between {lowest_num} and {highest_num}")
while is_running:
    try:
        guess = input("Enter number between 1 and 100: ")

        if guess.isdigit():
            guess = int(guess)
            guesses += 1
            if guess > highest_num or guess < lowest_num:
                print("Please enter number between 1 and 100...!")
                print("Try again...")
            elif guess > answer:
                print("Too High. Try again...!")
            elif guess < answer:
                print("Too low. Try again...!")
            else:
                print(f"Correct!. The answer was {answer}")
                print(f"Number guessing is {guesses}")
                is_running = False
    except ValueError:
        print("Invalid number...!")
        print("Please enter number between 1 and 100")
