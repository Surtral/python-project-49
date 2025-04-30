import random

def main():
    from brain_games.cli import welcome_user
    name = welcome_user()
    for _ in range(3):
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        operations = ['+', '-', '*', '//']
        operation = random.choice(operations)
        print("What is the result of the expression?")
        print(f'Question: {num1} {operation} {num2}')
        user_answer = int(input("Your answer: "))
        
        if operation == "+":
            result = num1 + num2 
        elif operation == "-":
            result = num1 - num2
        elif operation == "//":
            result = num1 // num2
        elif operation == "*":
            result = num1 * num2
    
        if user_answer == result:
            print("Correct!")
        else:
            print(f"{user_answer} is wrong answer :( The correct answer was '{result}'.")
            print(f"Let's try again, {name}.")
            break
    else:
        print(f"Congratulations, {name}!")




if __name__ == "__main__":
    main()