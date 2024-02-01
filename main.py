# from GameManager import GameManager
import time

from colorama import Fore, Back

from MultiChoice import MultiChoice
from Question import Question
from TorFquestion import TorFquestion
from utils import cprint

if __name__ == '__main__':
    questions = [
            Question("who was the first prime minister?", ['bibi', 'ben gurion', 'golda', 'sapir rondelim'], 2),
            Question("how many meters of depth are there in a goose?", ['bibi', '1', 'next question, please', '6'], 4),
            MultiChoice("who sat at Burekas Haagala 4 in the morning?", ["me", "itzik zino", "tsiyon malka", "mozart"],
                        [1, 2, 3]),
            TorFquestion("python is fun to use", True)
        ]
    run = True
    current_question = 0
    score = 0
    while run:
        if current_question == len(questions):
            print(f"{score} out of {len(questions)}")
            break
        question = questions[current_question]
        cprint(f"Question {current_question + 1}:", Fore.BLACK, Back.LIGHTGREEN_EX)
        time.sleep(1)
        question.show()
        answer = input("your answer: ")
        if answer == "quit":
            break

        result = question.check(answer)
        if result:
            cprint("well done! moving on...", Fore.GREEN)
            score += 1
        else:
            cprint("wrong answer! moving on...", Fore.RED)

        current_question += 1
