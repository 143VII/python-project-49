import random

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if is_prime(number) else 'no'
    return question, answer

def get_game_rules():
    return "Answer 'yes' if given number is prime. Otherwise answer 'no'."
