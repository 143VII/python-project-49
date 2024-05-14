#!/usr/bin/env python3
import random
from brain_games.engine import run

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

def main():
    game_rules = "What is the result of the expression?"
    run(generate_round, game_rules)

if __name__ == "__main__":
    main()
