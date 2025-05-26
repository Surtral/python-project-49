import math
import secrets

from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")

    for _ in range(3):
        a, b = secrets.randbelow(100) + 1, secrets.randbelow(100) + 1
        correct = math.gcd(a, b)
        print(f'Question: {a} {b}')
        ansver = input("Your answer: ").strip()

        if int(ansver) != correct:
            print(
                f"'{ansver}' is wrong answer ;(. "
                f"Correct answer was '{correct}'."
            )
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()