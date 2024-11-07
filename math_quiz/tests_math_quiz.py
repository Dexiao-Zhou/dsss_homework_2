import unittest
from math_quiz import random_integer, random_operator, problem_answer


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        operators = {"+", "-", "*"}
        for _ in range(1000):
            op = random_operator()
            self.assertIn(op, operators)

    def test_problem_answer(self):
        # Define test cases in the format: (num1, num2, operator, expected_problem, expected_answer)
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (7, 3, '-', '7 - 3', 4),
            (4, 6, '*', '4 * 6', 24),
            (10, 5, '+', '10 + 5', 15),
            (9, 3, '-', '9 - 3', 6),
            (3, 3, '*', '3 * 3', 9)
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = problem_answer(num1, num2, operator)
            # Check if the generated problem matches the expected problem string
            self.assertEqual(problem, expected_problem)
            # Check if the generated answer is correct
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
