#!/usr/bin/env python3

def ask_question(number, user_name):
    user_answer = input(f"Question: {number}\nYour answer: ")
    correct_answer = "yes" if number % 2 == 0 else "no"
    return user_answer.lower() == correct_answer


def main():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


    numbers = [15, 6, 7, 47, 66, 34, 74, 29]
    correct_answers = 0


    for number in numbers:

        
        if ask_question(number, user_name):
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