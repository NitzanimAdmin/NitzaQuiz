import os
from colorama import Fore, Back, Style
from utils import cprint


class Question(object):
    def __init__(self, question, answers, correct_index):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_index

    def show(self):
        cprint(self.question, Fore.BLUE)
        for index, answer in enumerate(self.answers):
            cprint(f'{index + 1} - {answer}', Fore.BLUE)

    def check(self, answer):
        return int(answer) == self.correct_answer
