import random
import secrets



def is_even(number):
    return number % 2 == 0


def main():
    from brain_games.cli import welcome_user
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(3):
        number = secrets.randbelow(100) + 1
        print(f'Question: {number}')
        user_answer = input("Is it even? (yes/no)")
        correct_answer = "yes" if is_even(number) else "no"
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"{user_answer} is wrong answer :( "
                f"The correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    main()