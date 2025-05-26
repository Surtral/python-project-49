import secrets

from brain_games.cli import welcome_user


def make_progression():
    start = secrets.randbelow(20) + 1
    step = secrets.randbelow(10) + 1
    length = secrets.randbelow(6) + 5
    missing_index = secrets.randbelow(length)
    
    progression = [start + step * i for i in range(length)]
    answer = progression[missing_index]
    progression[missing_index] = '..'
    
    return progression, answer


def main():
    name = welcome_user()
    print("What number is missing in the progression?")
    
    for _ in range(3):
        progression, answer = make_progression()
        print("Question:", ' '.join(map(str, progression)))
        
        user_answer = input("Your answer: ")
        if user_answer == str(answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{answer}'."
            )
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()