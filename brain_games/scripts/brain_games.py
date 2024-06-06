#!/usr/bin/env python3
from brain_games.scripts.brain_game import main


def main():
    print("Welcome to the Brain Games!")
    user_name = input("May I have your name? ")
    print(f"Hello, {user_name}!")

if __name__ == "__main__":
    main()