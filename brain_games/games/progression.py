#!/usr/bin/env python3
from random import randint


RULES_OF_GAME = 'What number is missing in the progression?'


def generate_question_answer():
    num1 = randint(1, 10)
    max_num_progression = 10
    progression = [num1, ]
    num_step = randint(1, max_num_progression - 1)
    random_index = randint(0, max_num_progression - 1)
    i = 1
    while i < max_num_progression:
        progression.append(progression[i - 1] + num_step)
        i += 1
    correct_answer = str(progression[random_index])
    progression[random_index] = '..'
    question2 = 'Question:'
    i = 0
    while i < max_num_progression:
        question2 = question2 + ' ' + str(progression[i])
        i += 1
    return question2, correct_answer
