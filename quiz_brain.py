class QuizBrain:
    def __init__(self, question_list: list):
        self.__question_list = question_list
        self.__question_number = 0
        self.__score = 0

    @property
    def question_list(self):
        return self.__question_list

    @property
    def question_number(self):
        return self.__question_number

    @property
    def score(self):
        return self.__score

    @question_number.setter
    def question_number(self, new_question_number):
        self.__question_number = new_question_number

    @score.setter
    def score(self, new_score):
        self.__score = new_score

    def next_question(self):
        question = self.question_list[self.question_number].question
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {question} (True/False)?: ")
        self.check_answer(user_answer, answer)

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer: str, correct_answer: bool):
        if user_answer.lower() == str(correct_answer).lower():
            self.score += 1
            print("You've got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
