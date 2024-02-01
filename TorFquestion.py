from Question import Question
from colorama import Fore, Back, Style
from utils import cprint


class TorFquestion(Question):
    def __init__(self, question, correct_answer):
        super().__init__(question, ["True", "False"], 0)
        self.correct_answer = correct_answer

    def show(self):
        cprint("Write True or False:", Fore.BLACK, Back.CYAN)
        super().show()

    def check(self, answer):
        return answer.lower() == str(self.correct_answer).lower()
