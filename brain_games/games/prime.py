from random import randint


RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_answer():
    num = randint(0, 10000)
    if num <= 1:
        correct_answer = 'no'
    else:
        for i in range(2, num):
            if (num % i) == 0:
                correct_answer = 'no'
                break
        else:
            correct_answer = 'yes'
    question2 = (f'Question: {num}')
    return question2, correct_answer
