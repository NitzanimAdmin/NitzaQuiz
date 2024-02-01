from colorama import Fore, Back

from Question import Question
from utils import cprint


class MultiChoice(Question):
    def __init__(self, question, answers, correct_list):
        super().__init__(question, answers, correct_list[0])
        self.correct_answers = correct_list

    def show(self):
        cprint("Multiple choice:", Fore.BLACK, Back.YELLOW)
        super().show()

    def check(self, answer):
        score = 0
        nums = set(int(ans) for ans in answer.split(","))
        for n in nums:
            if n in self.correct_answers:
                score += 1
        return score == len(self.correct_answers)
