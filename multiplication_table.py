import random

<<<<<<< HEAD
    # Generating two random numbers from 1 to 12, 12 inclusive
=======
    # Generating two random numbers from 1 to 12
>>>>>>> f6536cb24a61492fb973ddc2a0593bdce26cbabd
a = random.randint(1, 12)
b = random.randint(1, 12)

print(f"{a} x {b}")

guess = input("What is the answer? ")
guess = int(guess)

    # Multiplying the two numbers
total = a * b
if total == guess:
    print(f"Correct!!! The answer is {total}")
else:
    print(f"Oops, you lose!!! The answer is: {total}. \nTry again")
