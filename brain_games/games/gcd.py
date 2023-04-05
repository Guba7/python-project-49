from random import randint


RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    first_numb_rand = 1
    num1 = randint(first_numb_rand, 100)
    num2 = randint(first_numb_rand, 100)
    question2 = (f'Question: {num1} {num2}')
    if num1 < num2:
        num1, num2 = num2, num1
    question2 = (f'Question: {num1} {num2}')

    while num2 != 0:
        num1, num2 = num2, num1 % num2
    correct_answer = num1
    print(f'{correct_answer} = {num1}')
    return question2, correct_answer
