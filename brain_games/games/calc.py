import random


def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2

    question = f"{num1} {operator} {num2}"
    return question, str(correct_answer)


def get_game_rules():
    return "What is the result of the expression?"
