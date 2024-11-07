import random


def random_integer(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def random_operator():
    return random.choice(['+', '-', '*']) # select a random operator from  + - *


def problem_answer(num1, num2, operator):
    problem = f"{num1} {operator} {num2}"
    if operator == '+': answer = num1 + num2 # select three kinds of operation
    elif operator == '-': answer = num1 - num2
    else: answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    t_q = 3  # the quantity of the questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        num1 = random_integer(1, 10)
        num2 = random_integer(1, 5)
        operator = random_operator()

        problem, answer = problem_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        user_answer = input("Your answer: ")
        
        try:
            # the input must be greater than 0 
            user_answer = int(user_answer)
            if user_answer < 0:
                raise ValueError("The input value should be a positive integer.")
        except ValueError as e:
            print(f"Error: {e}")
            continue

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{t_q} ({(score/t_q)*100:.2f}%)")

# main function
if __name__ == "__main__":
    math_quiz()