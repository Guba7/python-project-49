#!/usr/bin/env python3
from random import randint


RULES_OF_GAME = 'What is the result of the expression?'


def generate_question_answer():
    num1 = randint(0, 10)
    num2 = randint(0, 10)
    oper = randint(1, 3)
    if oper == 1:
        symbol = '+'
        correct_answer = num1 + num2
    elif oper == 2:
        symbol = '-'
        correct_answer = num1 - num2
    else:
        symbol = '*'
        correct_answer = num1 * num2
    question2 = (f'Question: {num1} {symbol} {num2}')
    correct_answer = str(correct_answer)
    return question2, correct_answer
