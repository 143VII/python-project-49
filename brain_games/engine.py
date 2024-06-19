#!/usr/bin/env python3

def run(game, get_game_rules):
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(get_game_rules())

    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = game()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {user_name}!")
            return

    print(f"Congratulations, {user_name}!")
