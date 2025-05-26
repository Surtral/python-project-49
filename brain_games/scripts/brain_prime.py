import random

from brain_games.cli import welcome_user


def is_prime(number):
    if number <= 1: 
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def main():

    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(3):

        number = random.randint(1, 100)
        print(f"Question: {number}")
        
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = "yes" if is_prime(number) else "no"
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()