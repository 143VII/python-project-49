#!/usr/bin/env python3

def main():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")
    print("What number is missing in the progression?")

    progressions = ["5 7 9 11 13 .. 17 19 21 23", 
                    "2 5 8 .. 14 17 20 23 26 29", 
                    "14 19 24 29 34 39 44 49 54 .."]
    correct_answers = ["15", "11", "59"]

    for i in range(3):
        print(f"Question: {progressions[i]}")
        user_answer = input("Your answer: ")
        if user_answer == correct_answers[i]:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answers[i]}'.\nLet's try again, {user_name}!")

    print(f"Congratulations, {user_name}!")

if __name__ == "__main__":
    main()