import time

import colorama
from colorama import Fore, Back

from MultiChoice import MultiChoice
from Question import Question
from TorFquestion import TorFquestion
from utils import cprint, INTRO_TITLE


class GameManager(object):
    def __init__(self, path, mode="file"):
        if mode == "file":
            self.questions = self.load_question_file(path)
        elif mode == "test":
            self.questions = self.load_questions()
        self.current_question = 0
        self.score = 0
        self.max_score = sum([que.score for que in self.questions])

    def load_questions(self):
        return [
            Question("who was the first prime minister?", ['bibi', 'ben gurion', 'golda', 'sapir rondelim'], 2),
            Question("how many meters of depth are there in a goose?", ['bibi', '1', 'next question, please', '6'], 4),
            MultiChoice("who sat at Burekas Haagala 4 in the morning?", ["me", "itzik zino", "tsiyon malka", "mozart"],
                        [1, 2, 3]),
            TorFquestion("bush did 9/11", True)
        ]

    def load_question_file(self, path):
        questions = []
        with open(path, "r") as f:
            lines = f.readlines()
            for line in lines:
                data = line.split(",")
                if data[0] == '1':
                    questions.append(Question(data[1], data[2:-1], int(data[-1])))
                elif data[0] == '2':
                    answers = [int(ans) for ans in data[-1].split(";")]
                    questions.append(MultiChoice(data[1], data[2:-1], answers))
                elif data[0] == '3':
                    questions.append(TorFquestion(data[1], data[2].lower() == 'true'))
        return questions

    def run(self):
        colorama.init(autoreset=True)
        run = True
        cprint("Welcome to...", Fore.BLACK, Back.LIGHTCYAN_EX)
        time.sleep(1)
        cprint(INTRO_TITLE, Fore.CYAN)
        time.sleep(1)
        cprint("Are you ready?", Fore.BLACK, Back.LIGHTCYAN_EX)
        time.sleep(1)
        while run:
            if self.current_question >= len(self.questions):
                cprint(f"THE END! your score is {self.score} out of {self.max_score}", Fore.BLACK, Back.YELLOW)
                break

            question = self.questions[self.current_question]
            cprint(f"Question {self.current_question + 1}:", Fore.BLACK, Back.LIGHTGREEN_EX)
            time.sleep(1)
            question.show()
            answer = input("your answer: ")
            if answer == "quit":
                break

            result = question.check(answer)
            if result == question.score:
                cprint("well done! moving on...", Fore.GREEN)
            elif 0 < result < question.score:
                cprint("nice try, but this is partially correct", Fore.YELLOW)
            else:
                cprint("wrong answer! moving on...", Fore.RED)
            self.score += result
            self.current_question += 1
            time.sleep(1)
            