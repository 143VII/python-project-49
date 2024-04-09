#!/usr/bin/env python3
import math

def ask_question(numbers, user_name):
    gcd = math.gcd(*numbers)
    user_answer = input(f"Question: What is the greatest common divisor of {numbers}?\nYour answer: ")
    if int(user_answer) == gcd:
        print("Correct!")
        return True
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{gcd}'.\nLet's try again, {user_name}!")
        return False

def main():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Find the greatest common divisor of given numbers.")

    numbers_list = [[25, 50], [100, 52], [3, 9]]
    correct_answers = 0

    for numbers in numbers_list:
        if ask_question(numbers, user_name):
            correct_answers += 1
        else:
            correct_answers = 0
        if correct_answers == 3:
            print(f"Congratulations, {user_name}!")
            break

if __name__ == "__main__":
    main()