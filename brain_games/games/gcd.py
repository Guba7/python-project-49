#!/usr/bin/env python3
from random import randint
import math


def generate_question_answer():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    question1 = ('Find the greatest common divisor of given numbers.')
    question2 = (f'Question: {num1} {num2}')
    correct_answer = str(math.gcd(num1, num2))
    return question1, question2, correct_answer


def main():
    generate_question_answer()


if __name__ == '__main__':
    main()
