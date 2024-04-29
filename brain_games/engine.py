#!/usr/bin/env python3
import math

def ask_question(number, user_name):
    user_answer = input(f"Question: {number}\nYour answer: ")
    correct_answer = "yes" if number % 2 == 0 else "no"
    return user_answer.lower() == correct_answer

def ask_question_gcd(numbers, user_name):
    gcd = math.gcd(*numbers)
    user_answer = input(f"Question: What is the greatest common divisor of {numbers}?\nYour answer: ")
    return int(user_answer) == gcd

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
