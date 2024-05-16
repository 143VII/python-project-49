import random
import math

def generate_round():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f"{num1} {num2}"
    answer = str(math.gcd(num1, num2))
    return question, answer

def get_game_rules():
    return "Find the greatest common divisor of given numbers."
