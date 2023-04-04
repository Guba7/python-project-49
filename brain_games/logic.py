import prompt


ROUNDS_QUANTITY = 3


def logic_run(games):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(games.RULES_OF_GAME)
    i = 1
    while i <= ROUNDS_QUANTITY:
        question2, correct_answer = games.generate_question_answer()
        print(question2)
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
