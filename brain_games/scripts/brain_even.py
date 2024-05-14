#!/usr/bin/env python3

import random
from brain_games.engine import run

def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer

def main():
    game_rules = "Answer 'yes' if the number is even, otherwise answer 'no'."
    run(generate_round, game_rules)

if __name__ == "__main__":
    main()