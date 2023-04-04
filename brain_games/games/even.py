#!/usr/bin/env python3
import random


RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no" .'


def generate_question_answer():
    rnd_numb = random.randint(1, 100)
    question_2 = (f'Question: {rnd_numb}')
    if rnd_numb % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question_2, correct_answer
