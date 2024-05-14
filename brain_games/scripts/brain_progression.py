#!/usr/bin/env python3
import random
from brain_games.engine import run

def generate_round():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = random.randint(5, 10)
    missing_index = random.randint(0, length - 1)

    progression = [str(start + step * i) for i in range(length)]
    correct_answer = progression[missing_index]
    progression[missing_index] = '..'

    question = ' '.join(progression)
    return question, correct_answer

def main():
    game_rules = "What number is missing in the progression?"
    run(generate_round, game_rules)

if __name__ == "__main__":
    main()
