#!/usr/bin/env python3
from brain_games.engine import ask_question_gcd

def main():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Find the greatest common divisor of given numbers.")

    numbers_list = [[25, 50], [100, 52], [3, 9]]
    correct_answers = 0

    for numbers in numbers_list:
        if ask_question_gcd(numbers, user_name):
            print("Correct!")
            correct_answers += 1
        else:
            print("That's wrong, let's try again!")
            correct_answers = 0
        if correct_answers == 3:
            print(f"Congratulations, {user_name}!")
            break

if __name__ == "__main__":
    main()
