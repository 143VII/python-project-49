#!/usr/bin/env python3
from brain_games.engine import is_prime

def main():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")

    numbers = [2, 5, 24, 11, 6, 7, 17,]
    correct_answers = 0

    for number in numbers:
        print(f"Question: {number}")
        answer = input("Your answer: ")

        if is_prime(number):
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if answer == correct_answer:
            print("Correct!")
            correct_answers += 1
            if correct_answers == 3:
                print(f"Congratulations, {name}!")
                return
        else:
            print(f"Sorry, {name}, but your answer is incorrect.")
            print("Would you like to play again? (yes/no)")
            play_again = input()
            if play_again.lower() != 'yes':
                return

if __name__ == "__main__":
    main()
