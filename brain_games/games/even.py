import random

def generate_round():
    number = random.randint(1, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer

def get_game_rules():
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
