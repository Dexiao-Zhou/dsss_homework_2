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
        num1 = random_integer(1, 5)  # Generate a random integer between 1 and 5 for the first number
        num2 = random_integer(6, 10)  # Generate a random integer between 6 and 10 for the second number
        operator = random_operator()  # Select a random operator from '+', '-', or '*'

        # Generate the math problem and the correct answer based on num1, num2, and operator
        problem, answer = problem_answer(num1, num2, operator)
        print(f"\nQuestion: {problem}")  # Display the generated math question

        # Loop until a valid number is provided by the user
        while True:  
            user_answer = input("Your answer: ")  # Prompt the user to input their answer

            try:
                # Attempt to convert the input to an integer
                user_answer = int(user_answer)
                break  # Exit the loop if conversion is successful
            except ValueError:
                # Handle the case where the input is not a valid integer
                print("Invalid input. Please enter a number.")  # Prompt for a valid number

        # Check if the user's answer matches the correct answer
        if user_answer == answer:
            print("Correct! You earned a point.")  # Congratulate the user on a correct answer
            score += 1  # Increment the score by 1 for each correct answer
        else:
            # Inform the user of the correct answer if their answer is wrong
            print(f"Wrong answer. The correct answer is {answer}.")

# After all questions, display the user's final score and success rate as a percentage
    print(f"\nGame over! Your score is: {score}/{t_q} ({(score/t_q)*100:.2f}%)")

# Main function entry point to start the quiz
if __name__ == "__main__":
    math_quiz()