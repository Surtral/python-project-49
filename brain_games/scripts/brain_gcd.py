import math 
import random
from brain_games.cli import welcome_user

def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        a, b = random.randint(1,100), random.randint(1,100)
        correct = math.gcd(a,b)
        print(f'Queston: {a} {b}')
        ansver = input("Your answer: ").strip()

        if int(ansver) != correct:
            print(f"'{ansver}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
