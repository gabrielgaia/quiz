class Question:
    def __init__(self, question: str, answer: bool):
        self.__question = question
        self.__answer = answer

    @property
    def question(self):
        return self.__question

    @property
    def answer(self):
        return self.__answer
