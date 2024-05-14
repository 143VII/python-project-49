#!/usr/bin/env python3
import random
import math
from brain_games.engine import run

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer

def main():
    game_rules = "Find the greatest common divisor of given numbers."
    run(generate_round, game_rules)
if __name__ == "__main__":
    main()
