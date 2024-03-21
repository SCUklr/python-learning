# -*- coding = utf-8 -*-
# @Time : 2024/3/19 23:05
# @Author: Vast
# @File: survey.py
# @Software: PyCharm
class AnonymousSurvey:
    """收集匿名调查问卷的答案"""

    def __init__(self, question):
        """存出一个问题，并为储存答案做准备"""
        self.question = question
        self.responses = []

    def show_question(self):
        """显示调查问卷"""
        print(self.question)

    def store_response(self, r):
        self.responses.append(r)

    def show_results(self):
        """显示收集到的所有答卷"""
        print("Servey reults:")
        for r in self.responses:
            print(f'-{r}')
