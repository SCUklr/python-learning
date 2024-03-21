# -*- coding = utf-8 -*-
# @Time : 2024/3/19 23:30
# @Author: Vast
# @File: AnonymousServey.py
# @Software: PyCharm
import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""
    question = "What language did you first learn to speak?"

    language_survey = AnonymousSurvey(question)

    def test_store_single_response():
        """测试单个答案会被妥善地储存"""

        language_survey.store_response("English")
        assert 'English' in language_survey.responses

    def test_store_three_response():
        """测试三个答案会被妥善地储存"""

        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            language_survey.store_response(response)
        for response in responses:
            assert response in language_survey.responses
